__author__ = 'jay'

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('',

    #--------------------------------------------------------------------------------------------------
    # General Views
    #--------------------------------------------------------------------------------------------------
    url(r'^$',
        login_required(Index_View.as_view()),
        name="Index_View"),

    #--------------------------------------------------------------------------------------------------
    # List Views
    #--------------------------------------------------------------------------------------------------
    url(r'^venues/$',
        login_required(ListVenue_View.as_view()),
        name="ListVenue_View"),

    #--------------------------------------------------------------------------------------------------
    # Create/Edit Views
    #--------------------------------------------------------------------------------------------------
    url(r'^venues/create/$',
        login_required(CreateVenue_View.as_view()),
        name="CreateVenue_View"),

)