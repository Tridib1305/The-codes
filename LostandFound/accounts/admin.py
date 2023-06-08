from django.contrib import admin
from .models import Lost_Object

class Lost_ObjectAdmin(admin.ModelAdmin):
    list_display=('Product_Name', 'slug', 'Status', 'Lost_on')
    list_filter=("Status",)
    search_fields=['Product_Name', 'Description']
    prepopulated_fields={'slug':('Product_Name',)}

admin.site.register(Lost_Object, Lost_ObjectAdmin)

# Register your models here.
