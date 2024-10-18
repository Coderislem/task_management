from django.contrib import admin
from .models import CustomUser,ToDoList,Task,ActivityLog
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(ActivityLog)