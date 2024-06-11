from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
#This python class creates a User table that stores all the necessary user details, which are the username, first name, last name, and their email
#The username field is the primary key because it's unique.
class User(AbstractUser):

  username = models.CharField(max_length=50, unique=True)

  firstName = models.CharField(
                    max_length = 50
                )
  lastName = models.CharField(
           max_length = 50
       )

  user_email = models.EmailField(max_length = 254, null=True, blank=True)

  def __str__(self):
      return self.username

  def to_dict(self):
      return {
         'username': self.username,
      }

#This python class creates a tabled called TaskDetails that stores all the essential task details.
#The id field is included as a primary key to uniquely identify the task detail.
#The owner field is the foreign key that connects to the username, which is a primary key of the User table.
#The foreign key is needed to map the tasks details to the right user that it should belong to,
#or otherwise the database cannot know which task details belongs to which user.

class TaskDetails(models.Model):
      #     name = models.CharField(max_length=128)
      #     description = models.TextField()
      #     director = models.CharField(max_length=64)
      #     image = models.ImageField(upload_to='images/')
      #
      #     def __str__(self):
      #         return self.name

      id = models.BigAutoField(primary_key=True)
      name = models.TextField()
      date = models.DateField(auto_now=False)
      startTime = models.TimeField(auto_now=False)
      amountOfTime = models.TimeField(auto_now=False, auto_now_add=False)
      descriptionOfTheTask = models.TextField()
      image = models.ImageField(upload_to='images/')
      owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))

      def __str__(self):
          return f"({self.name})({self.date})({self.startTime})({self.amountOfTime})({self.descriptionOfTheTask})"

      def to_dict(self):
          return{
             'id': self.id,
             'name': self.name,
             'date':self.date,
             'startTime':self.startTime,
             'amountOfTime':self.amountOfTime,
             'descriptionOfTheTask':self.descriptionOfTheTask,
             'image': "http://localhost:8000/" +self.image.url,
           }

#This python class creates a table called CalorieDetail in the database, where all the calorie consumption details are recorded.
#The owner field is the foreign key that connects to the username primary key in the User table.
#The foreign key is needed to map the calorie consumption details to the right user that it should belong to,
#or otherwise the database cannot know which calorie consumption belongs to which user.

class CalorieDetail(models.Model):
   amountOfCalories = models.IntegerField()
   currentDate = models.DateTimeField(auto_now_add=True)
   owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=int(round((datetime.now().timestamp()))))

   def __str__(self):
       return f"({self.amountOfCalories}) ({self.currentDate}) ({self.owner})"

   def to_dict(self):
       return{
           'amountofcalories': self.amountOfCalories,
           'currentdate': self.currentDate
       }