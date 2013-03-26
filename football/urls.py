from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from acu.views import Index_View

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'football.views.home', name='home'),
    # url(r'^football/', include('football.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^login/$', login, name="Login_View"),
    url(r'^logout/$', logout_then_login, name="Logout_View"),
    url(r'^$', login_required(Index_View.as_view()), name="Index_View"),

    url(r'^acu/', include('acu.urls', namespace='acu', app_name='acu')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
