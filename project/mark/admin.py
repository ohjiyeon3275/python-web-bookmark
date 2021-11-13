from django.contrib import admin
from mark.models import Mark

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
