from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'applied_at')
    search_fields = ('full_name', 'email')
    readonly_fields = ('applied_at',)
