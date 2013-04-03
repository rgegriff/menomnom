from django.contrib import admin
from models import Location, LocationCategory, LocationHighlight, LocationHour, LocationSpecial, LocationPhotos, LocationMistake
from management.models import ManagerProfile
from django.contrib.contenttypes import generic

class HourInline( admin.TabularInline ):
    model = LocationHour
    field = ("day", ("opening_time", "closing_time",),)
    max_num = 7
    extra = 7
    ordering = ('day',)

class ManagerInline(admin.StackedInline):
    model = ManagerProfile
    max_num = 1
    exclude = ("biz_posts",)

class SpecialsInline( admin.TabularInline ):
    model = LocationSpecial
    extra = 1

class PhotosInline( admin.TabularInline ):
    model = LocationPhotos
    extra = 1

class LocationAdmin( admin.ModelAdmin ):
    filter_horizontal = ('category',)
    prepopulated_fields = {
        'slug' : ('name',)
    }
    inlines = [ManagerInline,HourInline, SpecialsInline, PhotosInline]
    fieldsets = (
        ("Basic Info",{
            'fields': (('name', 'slug'), 'category','description', ('street', "city", "state", "zip"), 'phone', 'logo' ),
            }),
        )

class LocationCategoryAdmin( admin.ModelAdmin ):
    prepopulated_fields = {'slug' : ('name',)}
    fields = ('name','slug')

class LocationMistakeAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "message")


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationCategory, LocationCategoryAdmin)
admin.site.register(LocationHighlight)
admin.site.register(LocationHour)

admin.site.register(LocationMistake, LocationMistakeAdmin)