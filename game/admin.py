from django.contrib import admin
from .models import Resource


#admin.site.register(Resource)

class ResourceAdmin(admin.ModelAdmin):
    fields = ['type']

admin.site.register(Resource, ResourceAdmin)