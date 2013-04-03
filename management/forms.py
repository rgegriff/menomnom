import floppyforms as forms
from django.forms.models import inlineformset_factory
import models
from directory.models import Location, LocationHour, LocationSpecial
from django.contrib.localflavor.us.forms import USPhoneNumberField

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location


class LocationGeneralForm(forms.ModelForm):
    phone = USPhoneNumberField()

    class Meta:
        model = Location
        fields = ['phone', 'description']
        widgets = {
            'description': forms.Textarea
        }


class LocationHourForm(forms.ModelForm):
    class Meta:
        model = LocationHour
        widgets = {
            'day': forms.HiddenInput(),
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'})
        }


class LocationSpecialForm(forms.ModelForm):
    description = forms.CharField(required=False,
        widget=forms.TextInput(attrs={
            'class': 'foodSpecial'
        }))

    class Meta:
        model = LocationSpecial
        fields = ['day', 'type', 'description']

class BulletinPostForm(forms.ModelForm):
    class Meta:
        model = models.BizPost
        fields = ['message']