from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
import datetime
from dateutil.relativedelta import relativedelta

class EmailForm(forms.Form):
    email = forms.EmailField(max_length=140)

    def clean(self):
        cleaned_data = super(EmailForm, self).clean()
        try:
            User.objects.get(email=cleaned_data['email'])
        except User.DoesNotExist:
            raise forms.ValidationError("No user with that email address")
        return cleaned_data

class PasswordResetForm(forms.Form):
    ERRORMSGS = {'username_taken':"Sorry, that username has been taken",
                 'underage': "Must be at least 13 years old to register.",
                 "password_mismatch" : "passwords do not match"}
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=90, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=90, required=True)

    def clean(self):
        cleaned_data = super(PasswordResetForm, self).clean()
        pass1 = cleaned_data["password1"]
        pass2 = cleaned_data['password2']
        if pass1 != pass2:
            raise forms.ValidationError(self.ERRORMSGS['password_mismatch'])
        return cleaned_data

class LoginForm(forms.Form):
    ERRORMSGS = {'invalidData':"The username or password is invalid",
                 'acctDisabled': "This account has been disabled"}

    username = forms.CharField(max_length=90, required=True)
    password = forms.CharField(max_length=90, widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError(self.ERRORMSGS['invalidData'])
        if not user.is_active:
            raise forms.ValidationError(self.ERRORMSGS['acctDisabled'])

        return cleaned_data

class RegistrationForm(forms.Form):
    ERRORMSGS = {'username_taken':"Sorry, that username has been taken",
                 'underage': "Must be at least 13 years old to register.",
                 "password_mismatch" : "passwords do not match"}
    username = forms.CharField(max_length=90, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=90, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=90, required=True)
    email = forms.EmailField(max_length=140, required=True)
    birthday = forms.DateField(required=True)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")
        birthday = cleaned_data.get("birthday")

        if User.objects.filter(username=username).count():
            raise forms.ValidationError(self.ERRORMSGS['username_taken'])
        if pass1 != pass2:
            raise forms.ValidationError(self.ERRORMSGS['password_mismatch'])
        if birthday is not None and (datetime.date.today() - relativedelta(years=13)) < birthday:
            raise forms.ValidationError(self.ERRORMSGS['underage'])
        return cleaned_data