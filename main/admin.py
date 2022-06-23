from django.contrib import admin
from main.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'address', 'studyed', 'job')
admin.site.register(Student, StudentAdmin)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'img')
admin.site.register(Info, InfoAdmin)