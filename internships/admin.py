from django.contrib import admin
from .models import Internship, Application


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'stipend', 'posted_by')
    search_fields = ('title',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'internship', 'applied_on')
