from django.views.generic import DetailView, ListView, View
from django.utils import timezone
from django import http
from models import Location, LocationSpecial, LocationCategory
from json import dumps
import datetime
from django.conf import settings
# Create your views here.

class DirectoryList(ListView):
    queryset = Location.objects.all().order_by("slug")
    template_name = "directory.html"



    def get_context_data(self, **kwargs):
        '''
        attach the category objects to the list
        '''
        tap = super(DirectoryList, self).get_context_data(**kwargs)
        tap['category_list'] = LocationCategory.objects.all()
        tap['site'] = settings.SITE_ID
        return tap


class DirectoryPageView(DetailView):
    model = Location
    template_name = "specific.html"


class SpecialsView(ListView):
    queryset = Location.objects.all().order_by('slug')
    template_name = "specials.html"

    def get_queryset(self):
        if self.request.flavour == "mobile":
            return Location.objects.filter(
                location_special__in=LocationSpecial.objects.filter(
                    day=timezone.localtime(timezone.now()).weekday()
                )
            ).order_by("name").distinct()
        else:
            return super(SpecialsView, self).get_queryset()

    def get_context_data(self, **kwargs):
        cd = super(SpecialsView, self).get_context_data(**kwargs)
        cd['curday'] = timezone.localtime(timezone.now()).weekday()

        return cd

class StarToggle(View):
    def get(self,*args, **kwargs):
        print dir(self)
        params = self.request.GET
        response = {'error':False}
        if params.get("id", False):
            special = LocationSpecial.objects.get(id=params['id'])
            user = self.request.user
            if not user.is_authenticated():
                response['msg'] = "user not authenticated"
                return http.HttpResponse(dumps(response))
            if user in special.stared_by.all():
                special.stared_by.remove(user)
                response['msg'] = "user stared special"
            else:
                special.stared_by.add(user)
                response['msg'] = "user unstared special"
            return http.HttpResponse(dumps(response))
        return http.HttpResponse(dumps(response))
