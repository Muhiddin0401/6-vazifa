from django.contrib import admin
from .models import *

class KompaniyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','birth_date','created_ed','updated_ed',)
    search_fields = ('title',)
    list_display_links = ('title',)

class AvtomabilAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'kuchi', 'kompaniya')
    search_fields = ('title',)
    list_filter = ('kompaniya',)
    list_display_links = ('title',)

admin.site.register(Kompaniya,KompaniyaAdmin)
admin.site.register(Avtomabil,AvtomabilAdmin)