__author__ = 'jay'

from django.views.generic import (TemplateView, FormView, CreateView, UpdateView, ListView, DetailView)

from acu import models as acuMod

class Index_View(TemplateView):
    template_name = "acu/index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Index_View, self).get_context_data(**kwargs)

        #profile = self.request.user.get_profile()

        context['contact'] = self.request.user.contact

        return context