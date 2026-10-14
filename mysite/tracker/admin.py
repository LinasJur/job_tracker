from django.contrib import admin
from .models import JobApplication, Note

class NoteInline(admin.TabularInline):
    model = Note
    extra = 0

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'status', 'created_at')
    inlines = [NoteInline]

admin.site.register(JobApplication, JobApplicationAdmin)
