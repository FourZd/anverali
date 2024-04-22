from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_info', 'experience')
    search_fields = ('id', 'name', 'contact_info')