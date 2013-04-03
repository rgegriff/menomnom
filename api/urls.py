from django.conf.urls import patterns, include, url
from api import EventResource, MessageResource, MistakeResource

event_resource = EventResource()
message_resource = MessageResource()
mistake_resource = MistakeResource()
urlpatterns = patterns('',
    url(r'^events/',  include(event_resource.urls)),
    url(r'^message/', include(message_resource.urls)),
    url(r'^mistakes/', include(mistake_resource.urls)),
    )