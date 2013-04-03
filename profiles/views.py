from django.views.generic import FormView, RedirectView, TemplateView
import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import models
from django.core.mail import send_mail as send
from django.http import Http404

class LoginPage(FormView):
    form_class = forms.LoginForm
    template_name = "login.html"
    success_url = '/management/'
    def get_success_url(self):
        if "next" in self.request.REQUEST:
            return self.request.REQUEST['next']
        else:
            return super(LoginPage, self).get_success_url()

    def get_context_data(self, **kwargs):
        cd = super(LoginPage, self).get_context_data(**kwargs)
        if "next" in self.request.REQUEST:
            cd['next'] =  self.request.REQUEST['next']
        cd['headline'] = "Sign In"
        return cd


    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
        login(self.request, user)

        return super(LoginPage, self).form_valid(form)

class RegistrationPage(FormView):
    form_class = forms.RegistrationForm
    template_name = "login.html"
    url = '/'
    def get_success_url(self):
        if "next" in self.request.REQUEST:
            return self.request.REQUEST['next']
        else:
            return super(RegistrationPage,self).get_success_url()

    def get_context_data(self, **kwargs):
        cd = super(RegistrationPage, self).get_context_data(**kwargs)
        if "next" in self.request.REQUEST:
            cd['next'] =  self.request.REQUEST['next']
        return cd


    def form_valid(self, form):
        data = form.cleaned_data
        newuser = User.objects.create_user(username=data['username'],
                                          email=data['email'],
                                          password=data['password1'])
        newprofile = newuser.get_profile()
        newprofile.birthday = data['birthday']
        newprofile.save()
        new_user = authenticate(username=data['username'],
            password=data['password1'])
        login(self.request, new_user)
        return super(RegistrationPage, self).form_valid(form)

class PasswordReset(FormView):
    form_class = forms.EmailForm
    template_name = "modal_page.html"
    success_url = "/forgot/complete/"

    def get_context_data(self, **kwargs):
        cd = super(PasswordReset, self).get_context_data(**kwargs)
        cd["headline"] = "Password Reset"
        cd['button'] = "I forgot my password"
        return cd

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.get(email=data['email'])
        try:
            pr = models.PasswordReset.objects.get(user=user)
        except models.PasswordReset.DoesNotExist:
            pr = models.PasswordReset(user=user)
        pr.save()
        message = "Your password can be reset at: %s"%("http://menomnom.com/forgot/"+pr.slug+"/")
        send("Menomnom | Password reset",
            message=message,
            from_email="info@menomnom.com",
            recipient_list=[data['email']]
        )
        return super(PasswordReset, self).form_valid(form)

class PasswordEmailSent(TemplateView):
    template_name = "modal_confirm.html"

    def get_context_data(self, **kwargs):
        cd = super(PasswordEmailSent, self).get_context_data(**kwargs)
        cd['headline'] = "Confirmation email sent"
        cd['message'] = "This page will redirect shortly"
        return cd

class ChangePassword(FormView):
    form_class = forms.PasswordResetForm
    template_name = "modal_page.html"
    success_url = "/forgot/changed/"


    def get_context_data(self, **kwargs):
        cd = super(ChangePassword, self).get_context_data(**kwargs)
        cd['headline'] = "Enter new password"
        cd['button'] = 'Submit'
        return cd

    def form_valid(self, form):
        data = form.cleaned_data
        try:
            record = models.PasswordReset.objects.get(slug=self.kwargs['slug'])
            u = record.user
            u.set_password(data['password1'])
            u.save()
            record.delete()
        except models.PasswordReset.DoesNotExist:
            raise Http404
        return super(ChangePassword, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        try:
            models.PasswordReset.objects.get(slug=kwargs['slug'])
        except models.PasswordReset.DoesNotExist:
            raise Http404
        return super(ChangePassword, self).get(request, *args, **kwargs)

class PasswordChanged(TemplateView):
    template_name = "modal_confirm.html"

    def get_context_data(self, **kwargs):
        cd = super(PasswordChanged, self).get_context_data(**kwargs)
        cd['headline'] = "Your password has been changed"
        cd['message'] = "This page will redirect shortly"
        return cd



class LogoutPage(RedirectView):
    url = "/"

    def get_redirect_url(self, **kwargs):
        if "next" in self.request.REQUEST:
            return self.request.REQUEST['next']
        else:
            return super(LogoutPage, self).get_redirect_url()

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutPage, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
