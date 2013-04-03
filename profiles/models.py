from django.db import models
from management.models import ManagerProfile
from directory.models import Location
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
import uuid

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    birthday = models.DateField(null=True, blank=True)
    manager_profile = models.ForeignKey(ManagerProfile, null=True, blank=True)

    def get_my_events(self):
        return self.user.attending_events.filter(start_time__gt=datetime.date.today()).order_by("start_time")

    def get_my_specials(self):
        return self.user.stared_specials.filter(day=datetime.date.today().weekday())

    def get_my_location_specials(self):
        my_specials = self.get_my_specials()
        return Location.objects.filter(location_special__in=my_specials)

    def __unicode__(self):
        return ", ".join([self.user.last_name,self.user.first_name])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

sluggen = lambda: uuid.uuid4().hex
class PasswordReset(models.Model):
    requested = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name="password_reset")
    slug = models.SlugField(max_length=32, default=sluggen)