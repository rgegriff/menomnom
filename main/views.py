# Create your views here.
from django.views.generic import ListView, FormView, TemplateView
from events.models import Event
from management.models import BizPost
from forms import *
from django.core.mail import send_mail as send
import datetime


class HomePage(TemplateView):
    template_name = 'index.html'

class ContactPage(FormView):
    template_name = "modal_page.html"
    success_url = "/contact_confirm/"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
         cd = super(ContactPage, self).get_context_data(**kwargs)
         cd['headline'] = "Contact Us!"
         cd['button'] = "Submit"
         return cd
    
    def form_valid(self, form):
        data = form.cleaned_data
        subject = "Contact Form Message"
        message = """
                From: %s
                Phone: %s
                Message: %s"""%(data['name'],data['phone'], data['message'])
        recp = ['adam@menomnom.com', 'george@menomnom.com', 'jerad@menomnom.com']
        sender = "info@menomnom.com"
        send(subject,message,sender,recp)
        return super(ContactPage, self).form_valid(form)

class ContactConfirm(TemplateView):
    template_name = "modal_confirm.html"

    def get_context_data(self, **kwargs):
        cd = super(ContactConfirm, self).get_context_data(**kwargs)
        cd['headline'] = "Message Sent"
        cd['message'] = "You will be redirected shortly"
        return cd

class SubmitEventPage(FormView):
    form_class = SubmitEventForm
    template_name = "modal_page.html"
    success_url = '/event-submitted/'

    def get_context_data(self, **kwargs):
        cd = super(SubmitEventPage, self).get_context_data(**kwargs)
        cd['headline'] = "Suggest an Event"
        cd['button'] = "Submit"
        return cd

    def form_valid(self, form):
        evnt = form.save(commit=False)
        evnt.confirmed = False
        evnt.save()
        subject = "Event \"%s\" Submitted"%evnt.name
        message = """
        View/edit this event at http://menomnom.com/admin/events/event/%s/
                """%(evnt.id)
        recp = ['adam@menomnom.com', 'george@menomnom.com', 'jerad@menomnom.com']
        sender = "info@menomnom.com"
        send(subject,message,sender,recp)
        return super(SubmitEventPage, self).form_valid(form)

class SubmittedEventPage(TemplateView):
    template_name = "modal_confirm.html"

    def get_context_data(self, **kwargs):
        cd = super(SubmittedEventPage, self).get_context_data(**kwargs)
        cd['headline'] = 'Thank You!'
        cd['message'] = "Your event has been submitted. This page will redirect shortly"
        return cd

class AboutPage(TemplateView):
    template_name = "about.html"