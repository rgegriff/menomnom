from events.models import Event
from directory.models import LocationMistake
from tastypie.resources import ModelResource
from events.models import Event
from socialize.models import Message
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.throttle import BaseThrottle




class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'

class MessageResource(ModelResource):
    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'
        filtering = {
            'id' : ('gt')
        }

        authorization = Authorization()
        authentication = Authentication()
        throttle = BaseThrottle(throttle_at=2,timeframe=30)

    def obj_create(self, bundle, request=None, **kwargs):
        return super(MessageResource, self).obj_create(bundle, request, user=request.user.get_profile())

    def dehydrate(self, bundle):
        bundle.data['username'] = bundle.obj.user.user.username
        bundle.data['message'] = bundle.data['message'].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&#39;").replace('"', "&quot;")
        return bundle

class MistakeResource(ModelResource):
    class Meta:
        queryset = LocationMistake.objects.all()
        resource_name = 'mistake'
        filtering = {
            'id' : ('gt')
        }

        authorization = Authorization()
        authentication = Authentication()
        throttle = BaseThrottle(throttle_at=2,timeframe=30)
