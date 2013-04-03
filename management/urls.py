from django.conf.urls import patterns, url
import views

urlpatterns = patterns("",
    url(r'^$', views.GeneralManagementPage.as_view()),
    url(r"^hours/$", views.HoursManagementPage.as_view()),
    url(r'^specials/$', views.SpecialsManagementPage.as_view()),
    url(r'^highlights/$', views.HighlightsManagementPage.as_view()),
    url(r'^bulletin/$', views.BulletinPost.as_view()),
)