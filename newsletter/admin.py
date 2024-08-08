from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_added')
    search_fields = ('email', 'name')
    list_filter = ('date_added',)
    ordering = ('-date_added',)
