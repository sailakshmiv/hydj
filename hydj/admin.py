from django.contrib import admin
from .models import Contents

class ContentsAdmin(admin.ModelAdmin):
    list_display = [ "title" ]

admin.site.register(Contents, ContentsAdmin)