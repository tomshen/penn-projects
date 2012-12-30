from projects.models import Project
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['name']}),
        ('Other information',{'fields':['sub_date'], 'classes':['collapse']}),
    ]
    list_display = ('name', 'authors', 'sub_date')
    list_filter = ['sub_date']
    search_fields = ['name']
    date_hierarchy = 'sub_date'

admin.site.register(Project, ProjectAdmin)