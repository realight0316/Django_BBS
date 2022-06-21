from django.contrib import admin
from .models import Company

# Register your models here.

class companyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_name', 'nation')

admin.site.register(Company, companyAdmin)