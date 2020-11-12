from django.contrib import admin
from .models import Ticket


class YourAdmin(admin.ModelAdmin):
    fields = ['movie', 'date', 'price', 'seats', 'num', 'total', 'email', 'name']
    readonly_fields = ['movie', 'date', 'price', 'seats', 'num', 'total', 'email', 'name']

admin.site.register(Ticket, YourAdmin)