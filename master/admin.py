from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_number', 'message')