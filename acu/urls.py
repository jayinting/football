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
    # Create/Edit Views
    #--------------------------------------------------------------------------------------------------
    url(r'^player/create/$',
        login_required(CreatePlayer_View.as_view()),
        name="CreatePlayer_View"),

)