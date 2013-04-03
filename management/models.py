from django.db import models
from directory.models import Location
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
import datetime
# Create your models here.

HOURS_BACK = 48


class ManagerProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='manager')
    location = models.OneToOneField(Location, related_name="manager", null=True, blank=True)
    credits = models.IntegerField(max_length=4)
    biz_posts = models.ManyToManyField("BizPost", related_name="manager", blank=True, null=True)

    def last_posts(self):
        return self.biz_posts.all().order_by("-post_time")[:6]

    def __unicode__(self):
        return "ManagerProfile " + self.user.username


class BizPost(models.Model):
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    message = models.TextField()
    post_time = models.DateTimeField(auto_now=True)
    url = models.URLField(null=True, blank=True)
    urltext = models.CharField(max_length=75,null=True, blank=True)
    objects = CurrentSiteManager('site')
