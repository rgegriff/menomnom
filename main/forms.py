from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField
#from directory.models import Location
from events.models import Event

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = USPhoneNumberField()
    message = forms.CharField(widget=forms.Textarea)


class SubmitEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('slug','img','attended_by','location','category','featured','confirmed')
