from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from contact.forms import SubscribeEmailForm, GetInTouchForm
from contact.models import SubscribeEmail, GetInTouch


class SubscribeEmailView(CreateView):
    model = SubscribeEmail
    form_class = SubscribeEmailForm

    def get_success_url(self):
        return reverse('home')


class GetInTouchView(CreateView):
    model = GetInTouch
    form_class = GetInTouchForm
    template_name = 'contact/contact.html'

    def get_success_url(self):
        return reverse('contact')
