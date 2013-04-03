from django.conf.urls import patterns, url
import views

urlpatterns = patterns("",
    url(r"^(?P<span>(daily|weekly))/$", views.EventView.as_view()),
    url(r"^(?P<span>(daily|weekly))/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/", views.EventDay.as_view()),
    url(r'^(?P<slug>(.*))/', views.EventDetailView.as_view())
    )