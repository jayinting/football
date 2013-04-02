__author__ = 'jay'

from django.views.generic import (TemplateView, FormView, CreateView, UpdateView, ListView, DetailView)
from django.core.urlresolvers import reverse

from acu import models as acuMod

class CreateVenue_View(CreateView):
    model = acuMod.Venue
    template_name = "acu/create/create_venue.html"
    success_url = '/'

    def form_invalid(self, form):
        return super(CreateVenue_View, self).form_invalid(form)