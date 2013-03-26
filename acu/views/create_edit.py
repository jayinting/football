__author__ = 'jay'

from django.views.generic import (TemplateView, FormView, CreateView, UpdateView, ListView, DetailView)

from acu import models as acuMod

class CreatePlayer_View(CreateView):
    model = acuMod.Player
    template_name = "acu/create_player.html"

    def form_invalid(self, form):
        return super(CreatePlayer_View, self).form_invalid(form)