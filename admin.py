from django.contrib import admin
from .models import *
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display=['name','Department']
    list_display_links=['Department']
    list_editable=['name']

class MessageAdmin(admin.ModelAdmin):
    list_display=['your_name','subject']

class RegisterAdmin(admin.ModelAdmin):
    list_display=['name','Doctor_name','Date']
    list_editable=['Doctor_name','Date']

admin.site.register(Department)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Registration,RegisterAdmin)
#admin.site.register(Appointment)
#admin.site.register(Patient)
