__author__ = 'jay'

from django.contrib import admin

from .models import *

class BaseAdmin(admin.ModelAdmin):
    pass
    #list_display = ('id', 'goal', 'method', 'rate_type', 'base_value')

admin.site.register(Contact, BaseAdmin)
admin.site.register(Player, BaseAdmin)
admin.site.register(Team, BaseAdmin)
admin.site.register(Venue, BaseAdmin)
admin.site.register(Event, BaseAdmin)
admin.site.register(Game, BaseAdmin)
admin.site.register(Stat, BaseAdmin)