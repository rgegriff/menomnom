from api import urls as apiurls
from events import urls as eventsurls
from directory import urls as directoryurls
from directory.views import SpecialsView, StarToggle
from profiles import views as profileviews
from socialize import urls as socialurls
from main import views as mainviews
from management.views import BulletinListView
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^about/$', mainviews.AboutPage.as_view()),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainviews.HomePage.as_view()),
    url(r'^adzone/', include('adzone.urls')),
    url(r'^api/', include(apiurls)),
    url(r'^bulletins/$', BulletinListView.as_view()),
    url(r'^contact/$', name='contact', view=mainviews.ContactPage.as_view()),
    url(r'^contact_confirm/$', name='contact-confirm', view=mainviews.ContactConfirm.as_view()),
    url(r'^directory/', include(directoryurls)),
    url(r'^events/', include(eventsurls)),
    url(r'^login/$', profileviews.LoginPage.as_view()),
    url(r'^logout/$', profileviews.LogoutPage.as_view()),
    url(r'^forgot/$', profileviews.PasswordReset.as_view()),
    url(r'^forgot/complete/$', profileviews.PasswordEmailSent.as_view()),
    url(r'^forgot/(?P<slug>[abcdef0-9]{32})/$',
           profileviews.ChangePassword.as_view()),
    url(r'^forgot/changed/$', profileviews.PasswordChanged.as_view()),
    url(r'^management/', include('management.urls')),
    url(r'^register/$', profileviews.RegistrationPage.as_view()),
    url(r'^specials/$', SpecialsView.as_view()),
    url(r'^specials/star/$', StarToggle.as_view()),
    url(r'^social/', include(socialurls)),
    url(r'^submit-event/$', mainviews.SubmitEventPage.as_view()),
    url(r'^event-submitted/$',
        name="event-submitted",
        view=mainviews.SubmittedEventPage.as_view()),
)
