from django.contrib import admin
from .models import Kurs,Student

class KursAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start', 'stop','totalStudent', 'create_ed','update_ed')
    search_fields = ('title',)
    list_filter = ('start','stop')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'kurs', 'create_ed')
    search_fields = ('fullname', 'kurs__title')
    list_filter = ('kurs',)

admin.site.register(Kurs,KursAdmin)
admin.site.register(Student,StudentAdmin)