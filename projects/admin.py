from projects.models import Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['approved', 'name', 'authors', 'pitch']}),
        ('Other information',{'fields':['description', 'album_url', 'source_url', 'demo_url', 'thumbnail_url'], 'classes':['collapse']}),
    ]
    list_display = ('name', 'authors', 'sub_date', 'approved')
    list_filter = ['sub_date', 'approved']
    search_fields = ['name', 'authors']
    date_hierarchy = 'sub_date'

admin.site.register(Project, ProjectAdmin)