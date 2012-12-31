from projects.models import Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['approved', 'name', 'authors', 'sub_date', 'pitch']}),
        ('Other information',{'fields':['description', 'album_url', 'source_url', 'demo_url', 'thumb_url'], 'classes':['collapse']}),
    ]
    list_display = ('name', 'authors', 'sub_date')
    list_filter = ['sub_date']
    search_fields = ['name', 'authors']
    date_hierarchy = 'sub_date'

admin.site.register(Project, ProjectAdmin)