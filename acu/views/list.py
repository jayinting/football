__author__ = 'jay'

from django.views.generic import (TemplateView, FormView, CreateView, UpdateView, ListView, DetailView)
from django.core.urlresolvers import reverse
from django.db.models import Q

from acu import models as acuMod

class ListVenue_View(ListView):
    model = acuMod.Venue
    context_object_name = "venues"
    template_name = "acu/lists/venues.html"

    extra_refer ="&searchTerm=%s&col=%s&ot=%s"
    header_refer = "&searchTerm=%s"

    paginate_by = 10
    default_status = int(0)

    col_field_map = {1:'name',
                     2:'description',
                     }

    def get_queryset(self):

        profile = self.request.user.get_profile()

        venues = acuMod.Venue.objects.all()

        # If the user entered a search term, filter by that term
        search_term = self.request.GET.get('searchTerm', None)
        if search_term:
            venues = venues.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))

        defaultSort="desc"
        sortOrder = self.request.GET.get('ot', ('desc' if defaultSort=='desc' else 'asc'))
        nextOrder = ('asc' if sortOrder=='desc' else 'desc')
        self.sortOrder = sortOrder
        self.nextOrder = nextOrder

        #Order columns based on Header information
        #get column number - use Name of campaign if not found
        column = self.request.GET.get('col', 1)

        try:
            column = int(column)
        except ValueError:
            column = 1

        self.column = column

        asc = False
        if sortOrder == 'asc':
            asc = True

        sortField = self.col_field_map[column] if asc else "-" + self.col_field_map[column]

        venues = venues.order_by(sortField)

        return venues

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListVenue_View, self).get_context_data(**kwargs)

        context['search_term'] = self.request.GET.get('searchTerm', "")
        context['col'] = self.column
        context['nextOrder'] = self.nextOrder
        context['sortOrder'] = self.sortOrder
        context['header_refer'] = self.header_refer % (context['search_term'])
        context['extra_refer'] = self.extra_refer % (context['search_term'], context['col'], context['sortOrder'] )

        #if self.request.is_ajax():
        #    self.template_name = "up_audience_activator/proposals/proposal_list_table.html"

        return context