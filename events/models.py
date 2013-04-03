from django.db import models
from directory.models import Location
from django.contrib.auth.models import User
import datetime
from django_thumbs.db.models import ImageWithThumbsField
from itertools import groupby
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.utils import timezone
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
# Create your models here.

class EventManager(CurrentSiteManager):
    def get_events_for_today(self):
        return self.get_events_for_date(date=datetime.date.today())

    def get_events_for_date(self, date):
        return self.get_events_for_timespan(startdate=date, days=0)

    def get_events_for_week(self, date):
        return self.get_events_for_timespan(startdate=date, weeks=1)

    def get_events_for_timespan(self,startdate,days=0, weeks=0):
        RANGE = {}
        startdate = datetime.datetime.combine(
            date=startdate,
            time=datetime.time.min
        )
        enddate = datetime.datetime.combine(
            date=startdate,
            time=datetime.time.max
        )
        DELTA = relativedelta(weeks=weeks, days=days)
        RANGE['min'] = timezone.make_aware(startdate, timezone.get_current_timezone())
        RANGE['max'] = timezone.make_aware(enddate + DELTA, timezone.get_current_timezone())
        return self.get_query_set().filter( start_time__range=( RANGE['min'], RANGE['max'] ) )

    def get_query_set(self):
        return super(EventManager, self).get_query_set().exclude(confirmed=False)


class Event(models.Model):
    name = models.CharField(max_length=240)
    slug = models.SlugField(unique=True, null=True)
    img = ImageWithThumbsField(upload_to='eventpics', sizes=((144,144),(200,200)), null=True, blank=True)
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    location = models.ForeignKey('EventLocation', null=True)
    category = models.ForeignKey("EventCategory", null=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    confirmed = models.BooleanField(default=True, blank=True)
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    objects=CurrentSiteManager('site')
    confirmed_objects = EventManager()

    def extract_date(self):
        return self.start_time.date()

    def __unicode__(self):
        return self.name + " on " + self.start_time.strftime("%m/%d/%y")

class EventLocation(models.Model):
    HELP = {'dir_location': "If the location exists in directory, fill this."
                            " Otherwise, fill the rest of the entries"}

    #if event is in directory
    dir_location = models.ForeignKey(Location, null=True, blank=True, help_text=HELP['dir_location'])

    name = models.CharField(max_length=240, null=True, blank=True)
    address  = models.CharField(max_length=240,null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        if self.dir_location:
            return self.dir_location.name
        else:
            return self.name

class EventCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    icon = models.ImageField(upload_to="icons/event/")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "event categories"
