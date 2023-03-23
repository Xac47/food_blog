from django.shortcuts import render
from django.views.generic import ListView

from about.models import About


class AboutView(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'about/about.html'

    def get_queryset(self):
        return About.objects.first()
