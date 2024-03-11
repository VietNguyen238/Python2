from django.contrib import admin
from .models import NhatKy
# Register your models here.
class NhatKyAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']
admin.site.register(NhatKy, NhatKyAdmin)