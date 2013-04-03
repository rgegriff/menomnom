from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
import datetime
from south.modelsinspector import add_introspection_rules
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail as send
from django.utils import timezone
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

add_introspection_rules(
    [
        (
            (ImageWithThumbsField, ),
            [],
                {
                "verbose_name": ["verbose_name", {"default": None}],
                "name":         ["name",         {"default": None}],
                "width_field":  ["width_field",  {"default": None}],
                "height_field": ["height_field", {"default": None}],
                "sizes":        ["sizes",        {"default": None}],
                },
            ),
    ],
    ["^django_thumbs.db.models.ImageWithThumbsField",])

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ManyToManyField("LocationCategory")
    description = models.TextField(max_length=350, blank=True, null=True)
    street = models.TextField()
    city = models.CharField(max_length=200, default="Menomonie")
    state = models.CharField(max_length=2, default="Wi")
    zip = models.CharField(max_length=5, default="54751")
    phone = models.CharField(max_length=20)
    logo = ImageWithThumbsField(upload_to="locationimages", null=True, blank=True, sizes=((148,148),))
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    objects = CurrentSiteManager('site')

    def is_open(self):
        cur_time = datetime.datetime.now()
        day_code = cur_time.weekday()
        today_hrs = self.location_hour.get(day=day_code)
        yest_hrs = self.location_hour.get(day=(day_code-1)%7)
        #Is the current time between Today's open and closed?
        if today_hrs.opening_time < cur_time.time() < (today_hrs.closing_time if today_hrs.closing_time > today_hrs.opening_time else datetime.time.max):
            return True
        if yest_hrs.is_rollover():
            if cur_time.time() < yest_hrs.closing_time:
                return True
        return False


    def specials_today(self):
        weekday = timezone.localtime(timezone.now()).weekday()
        return self.location_special.filter(day=weekday)

    def food_special_days(self):
        return list(set([s.day_name() for s in self.location_special.food()]))

    def drink_special_days(self):
        return list(set([s.day_name() for s in self.location_special.drink()]))

    def special_days(self):
        return list(set([s.day_name() for s in self.location_special.all()]))


    def recent_posts(self):
        RANGE = {}
        startdate = datetime.datetime.today()
        DELTA = datetime.timedelta(hours=48)
        RANGE['min'] = datetime.datetime.combine(date=(startdate - DELTA).date(), time=datetime.time.min)
        RANGE['max'] = datetime.datetime.combine(date=(startdate), time=datetime.time.max)
        d = self.manager.biz_posts.filter( post_time__range=(RANGE['min'], RANGE['max'])).order_by("-post_time")
        return d

    def __unicode__(self):
        return self.name



class LocationPhotos(models.Model):
    location = models.ForeignKey(Location, related_name="location_photos")
    caption = models.CharField(max_length=140)
    image = ImageWithThumbsField(upload_to="locationphotos", sizes=((280,280),))

    def __unicode__(self):
        return "Image from " + self.location.name

class LocationCategory(models.Model):
    name = models.CharField(max_length=45)
    slug = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Location categories"


class LocationSpecialManager(CurrentSiteManager):
    use_for_related_fields = True

    def today(self):
        day = datetime.datetime.today().weekday()
        return super(LocationSpecialManager, self).all().filter(day=day)

    def food(self):
        return super(LocationSpecialManager, self).all().filter(type__exact="food")

    def drink(self):
        return super(LocationSpecialManager, self).all().filter(type__exact="drink")

class LocationSpecial(models.Model):
    DAY_CHOICES = ((0, "Monday"),
                   (1, "Tuesday"),
                   (2, "Wednesday"),
                   (3, "Thursday"),
                   (4, "Friday"),
                   (5, "Saturday"),
                   (6, "Sunday"))
    location = models.ForeignKey(Location, related_name="location_special")
    day = models.IntegerField(max_length=1, choices=DAY_CHOICES)
    type = models.CharField(max_length=5, choices=(('food', 'Food'),('drink', "Drink")))
    description = models.TextField()
    stared_by = models.ManyToManyField(User, null=True, blank=True, related_name="stared_specials")
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    objects = LocationSpecialManager('site')


    def day_name(self):
        DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return DAYS[self.day]

    def __unicode__(self):
        return self.location.name + " Special"


class LocationHighlight(models.Model):
    location = models.ForeignKey(Location, related_name="location_highlights")
    description = models.CharField(max_length=75)

    def __unicode__(self):
        return " highlight"

class LocationHour(models.Model):
    DAY_CHOICES = ((0, "Monday"),
                   (1, "Tuesday"),
                   (2, "Wednesday"),
                   (3, "Thursday"),
                   (4, "Friday"),
                   (5, "Saturday"),
                   (6, "Sunday"))
    location = models.ForeignKey(Location, related_name="location_hour")
    day = models.IntegerField(max_length=1, choices=DAY_CHOICES)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        ordering = ['day']

    def day_name(self):
        DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return DAYS[self.day]

    def is_rollover(self):
        """returns true if location closes after midnight"""
        return self.opening_time > self.closing_time

class LocationMistake(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __unicode__(self):
        return self.timestamp.strftime("%c")

    def save(self,**kwargs):
        subject = "Location Mistake Report"
        to_addrs = [i[1] for i in settings.ADMINS]
        send(subject, self.message, 'info@menomnom.com', to_addrs)
        super(LocationMistake, self).save(**kwargs)

