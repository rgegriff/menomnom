from django.views.generic import TemplateView, ListView, DetailView
from models import Event
import datetime, calendar
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
# Create your views here.

def generate_upcoming_spans(startdate=datetime.date.today(), span='daily'):

    intervals = 7 if span == "daily" else 4
    skip = timedelta(days=1) if span == 'daily' else timedelta(weeks=1)
    spans = []
    for step in range(intervals):
        d = timezone.localtime((timezone.now() + (skip*step)))
        spans.append({"date":d,
                      "dayname":d.strftime("%A") if span=='daily' else (d.strftime("%b %e - ") + (d+skip).strftime("%b %e"))})

    spans[0]['dayname'] = "Today" if span == "daily" else "This Week"
    spans[1]['dayname'] = "Tomorrow" if span == "daily" else "Next Week"
    return spans


class EventView(ListView):
    template_name = "events.html"

    def get_queryset(self):
        if self.kwargs['span'] == 'daily':
            return Event.confirmed_objects.get_events_for_date(timezone.now()).filter(site=settings.SITE_ID).order_by("start_time")
        else:
            return Event.confirmed_objects.get_events_for_week(timezone.now()).filter(site=settings.SITE_ID).order_by("start_time")

    def get_context_data(self, **kwargs):
        cd = super(EventView, self).get_context_data(**kwargs)
        if self.kwargs['span'] == 'daily':
            cd['spans'] = generate_upcoming_spans()
            cd['page_type'] = 'daily'
            cd['other'] = 'weekly'
        else:
            cd['spans'] = generate_upcoming_spans(span='weekly')
            cd['page_type'] = 'weekly'
            cd['other'] = 'daily'
        return cd


class EventDay(ListView):
    '''Returns the events for a particular day.'''

    def get_template_names(self):
        if self.request.is_ajax():
            return ['event_list.html']
        else:
            return ['events.html']

    def get_queryset(self):
        year, month, day = int(self.kwargs['year']), int(self.kwargs['month']), int(self.kwargs['day'])
        target_day = datetime.datetime(year,month,day) #'stupid' date type
        if self.kwargs['span'] == 'daily':
            return Event.confirmed_objects.get_events_for_date(target_day).order_by("start_time")
        else:
            return Event.confirmed_objects.get_events_for_week(target_day).order_by("start_time")

class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"