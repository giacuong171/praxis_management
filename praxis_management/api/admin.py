from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','date_of_birth','phone_number',
                    'next_appointment','paid','total_due','fully_paid','actual_pay']
    search_fields = ['phone_number']


admin.site.register(User, UserAdmin)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient,PatientAdmin)
