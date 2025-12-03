from django.contrib import admin
from app import models
# Register your models here.
class student_admin(admin.ModelAdmin):
    list_display=['name', 'roll_number']
admin.site.register(models.students,student_admin)