from django.contrib import admin
from tasks.models import *

# Register your models here.
@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    List_display = ('id' , 'title' ,'description' )
