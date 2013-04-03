from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
# Create your models here.


class MessageManager(models.Manager):

    def recent_posts(self):
        return super(MessageManager, self).get_query_set().order_by('-posted')[:20]

class Message(models.Model):
    user = models.ForeignKey(UserProfile)
    posted = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=240)

    objects = MessageManager()

