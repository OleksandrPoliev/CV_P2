from django.contrib import admin
from .models import Contact,FilesAdmin,Techskils,FRAMEWORK,TOOLS
# Register your models here.

admin.site.register(Contact)
admin.site.register(FilesAdmin)
admin.site.register(Techskils)
admin.site.register(FRAMEWORK)
admin.site.register(TOOLS)