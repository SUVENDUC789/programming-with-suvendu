from django.contrib import admin
from home.models import Contact
# Register your models here.

# admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','message','date')

admin.site.register(Contact,ContactAdmin)

