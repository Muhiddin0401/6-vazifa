from django.contrib import admin
from .models import *

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)

class newsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_ed', 'category', 'is_bool')
    search_fields = ('title',)
    list_filter = ('category',)

admin.site.register(Categories,categoryAdmin)
admin.site.register(News,newsAdmin)