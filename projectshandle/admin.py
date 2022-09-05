from django.contrib import admin
from projectshandle.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=('ptitle','pdesc','ppic','giturl')

admin.site.register(Project,ProjectAdmin)