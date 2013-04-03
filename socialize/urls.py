from django.conf.urls import patterns, url
import views

urlpatterns = patterns("",
    url(r'^$', views.MessageList.as_view()),
)