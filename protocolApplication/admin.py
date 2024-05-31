from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from protocolApplication.models import User,TaskDetails,CalorieDetail

# Register your models here.
admin.site.register(User, UserAdmin)

#admin.site.register(TaskDetails)
@admin.register(TaskDetails)
class TaskDetails(admin.ModelAdmin):
   list_display = ['name', 'date', 'startTime', 'amountOfTime', 'descriptionOfTheTask', 'image', 'owner']

@admin.register(CalorieDetail)
class CalorieDetail(admin.ModelAdmin):
   list_display = ['amountOfCalories', 'currentDate', 'owner']