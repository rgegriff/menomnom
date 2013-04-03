from django.contrib import admin
from models import Event, EventCategory, EventLocation

class LocationInline(admin.TabularInline):
    model = EventLocation
    max_num = 1

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'confirmed']
    prepopulated_fields = {'slug':['name']}

admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory)
admin.site.register(EventLocation)