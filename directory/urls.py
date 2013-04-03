from django.conf.urls import patterns, url
import views

urlpatterns = patterns("",
    url(r"^$", views.DirectoryList.as_view()),
    url(r"^(?P<slug>.*)/$", views.DirectoryPageView.as_view()),
)