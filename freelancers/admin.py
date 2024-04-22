from django.contrib import admin
from .models import Freelancer

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_info', 'experience')
    search_fields = ('id', 'name', 'contact_info')