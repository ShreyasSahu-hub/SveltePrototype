""" from django.shortcuts import render
from django.http import HttpResponse """

from django.shortcuts import render
from rest_framework import generics
from protocolApplication.models import TaskDetails, User, CalorieDetail
from protocolApplication.serializers import TaskSerializer
from rest_framework import viewsets
from .forms import SignUpForm, LoginPage
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

import unittest
from django.test.runner import DiscoverRunner
#from test_selenium import SeleniumTests

from .tests import SeleniumTests             #The SeleniumTests class is imported from the tests.py file

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskSerializer


#This python function runs the automated testing on the tests.py file


#This is a Django decorator that allows the Django code and the Vue.js code to communicate
@csrf_exempt
def print_test_results(request: HttpRequest) -> HttpResponse:

   if request.method == 'GET':

      test_case = SeleniumTests()
      results = {}

      # Call each test method and store the results
      results = test_case.testCRUDOperation()

      print(results)

      """

      results["Calorie Tracker Operation"] = test_case.testCalorieTrackerOperation()

      print(results["Calorie Tracker Operation"])

      results["Exercising Videos"] = test_case.testExercising_videos()

      print(results["Exercising Videos"])

      """

      #The result of the automated testing is returned in a JSON format,
      #for the function called tests is implemented in the MainPage.svelte file so it can access it.
      return JsonResponse({

         'test_results':[

             results

         ]

      })


#This is the SignUp function that is used to store the user's details in the database

def SignUp(request: HttpRequest) -> HttpResponse:

    form = SignUpForm()          #This is the class imported from the forms.py file used for the sign up field structure



    #The GET http method is used to retrieve the sign up page by passing the sign up fields to render the page
    #and requesting the html file located in the protocolApplication folder.

    if request.method == 'GET':
        return render(request, "protocolApplication/signup.html", {
            "form": form,
        })


    #The POST http request is used to saves whatever details the user typed in the sign up form in the database.
    if request.method == 'POST':
        form = SignUpForm(request.POST)



        #The if statement checks if the POST https request works. If it works then it captures whatever details that the user has typed in the form
        if form.is_valid():
             firstName = form.cleaned_data['firstName']
             lastName = form.cleaned_data['lastName']
             username = form.cleaned_data['username']
             email = form.cleaned_data['user_email']
             password = form.cleaned_data['password']
             password_confirm = form.cleaned_data['password_confirm']



             #The if statement checks if the password is matched to the confirmed password. If it's matched then the user's details are saved in the database.
             #If the username is not unique then an error message is displayed saying to the user that you need to type another username is the form because according to the username property in the database,
             #it's a primary key and a primary key is required to be unique.
             #If the password and the confirmed password is not matched then an error message is displayed to the user that the password doesn't match.
             if password == password_confirm:
               try:
                 CreateUser = User.objects.create(firstName=firstName, lastName=lastName, username=username, user_email=email)
                 CreateUser.set_password(password)
                 CreateUser.save()
               except:
                     return HttpResponse("The username is already taken. Please type another username")



             #The user details are authenticated using the authenticate function from the auth class, which is imported from the django.contrib library.
             user = auth.authenticate(firstName=firstName, lastName=lastName, username=username, user_email=email, password=password, password_confirm=password)


             #It checks if the user details are not empty. If it's not, then it redirects the user to the login page.
             if user is not None:
                 auth.login(request, user)
                 #return redirect('/login')
                 return redirect('/login')
             return HttpResponse("Password doesn't match")



#This Login function is used to verify and authenticate the user's credentials, by comparing it to the stored credentials in the database

def Login(request: HttpRequest) -> HttpResponse:

   form = LoginPage()              #This is the LoginPage class that is imported from the forms.py file that is used for the field structure in login page.



   #The GET http request is used to fetch the login page by locating the login.html file in the protocolApplication folder
   #and passing all the essential fields that are inside the LoginPage class
   if request.method == 'GET':
        return render(request, "protocolApplication/login.html", {
            "form": form,
        })



   #The POST http request is used to authenticate the user credentials by comparing the username and password that are typed on the login page
   #and the username and password that are stored in the database
   if request.method == 'POST':
        form = LoginPage(request.POST)
        #PermissionChecker = User.objects.get()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)           #This is where the comparison is done

            print("sfbsdfbsdtgn: " + str(user is not None))

            print("serfbsetfbsetbn" + str(request.user))

            UserObjectEmail = User.objects.filter(username=username).values("user_email")



            #If the comparison is matched then the user is redirected to the main page
            if user is not None:

                 auth.login(request, user)

                 return redirect('http://localhost:8080/#/mainpage')

            try:

               print(UserObjectEmail[0]['user_email'])

            except:

                return HttpResponse("The user doesn't exist")

            else:
                return render(request, "protocolApplication/login.html", {
                     "form": form,
                })

#             if user is not None and UserObject[0]['UserType']=='0':
#                 auth.login(request, user)
#                 #return HttpResponse("User logged in")
#                 return redirect('/fooddonor')
#                 #return render(request, "mywebsite/fooddonor/index.html", {})
#                 #spa_view(request)
#             if user is not None and UserObject[0]['UserType']=='1':
#                 auth.login(request, user)
#                 ExpiringDateForPurchasedFoodItem = "This is a reminder that your purchased items will expire soon: "
#                 Email = UserObjectEmail[0]['user_email']
#                 for expiredate in ExpiringDateTracker.objects.all():
#
#                  if expiredate.owner.username==username:
#                   Email = expiredate.owner.user_email
#                   #NameForPurchasedFoodItem+=str(expiredate.PurchasedFoodItem)
#                   ExpiringDateForPurchasedFoodItem+=" \n Purchased food item: " + str(expiredate.PurchasedFoodItem) + ", ExpiringDate: " + str(expiredate.ExpiringDate) + " "

                 #else:
                   #ExpiringDateForPurchasedFoodItem+="You haven't filled any purchased item in the expiring date tracker"
                   #break

#                 SERVER = "smtp.gmail.com"
#                 server = smtplib.SMTP(SERVER, 587)
#                 email_from = 'sahushreyas74@gmail.com'
#                 server.ehlo()
#                 server.starttls()
#                 server.ehlo()
#                 server.login(email_from, "swuvrtgmerpiswna")
#                 subject = 'Expiring date reminder'
#                 message = ExpiringDateForPurchasedFoodItem
#
#                 msg = MIMEMultipart()
#                 msg['From'] = email_from
#                 msg['To'] = Email
#                 msg['Subject'] = subject
#
#                 msg.attach(MIMEText(message, 'plain'))
#
#                 print("hiiiiiiiiiiiiiiiiiiiiii",email_from)
#                 print(message)
#                 recipient_list = [Email]
#                 myset = set(recipient_list)
#                 text = msg.as_string()
#                 server.sendmail(email_from, myset, text)
#                 server.quit()
#                 #return redirect('http://localhost:5173/household')
#                 #return render(request, "mywebsite/household/index.html", {})
#                 return redirect('/household')
#                 #spa_view(request)
#                 #return render(request, "", {'frontend/index2.html'})
#             #return render(request, 'error.html', {
#                      #'error': 'User not registered. Sign up first.'
#             #})
#
#         #return render(request, 'mywebsite/login.html', {
#                     #'form': form
#         #})

        return HttpResponse("Failed to login. It is either you didn't type the password correctly or didn't type the username correctly. \n Please go back to the login page and type correctly")


#This function is used to add the task to the database
@csrf_exempt
def AddTask(request:HttpRequest) -> HttpResponse:

        print(request.user)


        #The request method is received from the handleSubmit function in the MainPage.svelte file and it checks whether it's a http POST request.
        if request.method == 'POST':

           #console.log("srfbgsdzrfbhsdtfb")

           print("asrfbrsetn")



           #If the http request is POST then the task details are saved in the database.
           #The owner field will store the username, to remember which user posted the user.
           taskdetail = TaskDetails.objects.create(
               name = request.POST['name'],
               date = request.POST['date'],
               startTime = request.POST['startTime'],
               amountOfTime = request.POST['amountOfTime'],
               descriptionOfTheTask = request.POST['descriptionOfTheTask'],
               image = request.FILES['image'],
               owner = request.user
           )

           taskdetail.save()

           print("sdfbsdfb")


           #The function returns the task detail in a JSON format, for the function called handleSubmit in the MainPage.svelte to access it
           #The JSON format is chosen so the task details will be more readable and easier to access its fields.
           return JsonResponse({

              'task_detail':[

                   taskdetail.to_dict()

              ]

           })


        #If the request method is not POST then the task details doesn't gets stored in the database.
        return JsonResponse({
              'task_detail':[

               "The task details are not added yet"

              ]
         })

#This function is used to fetch the tasks details from the database
@csrf_exempt
def FetchTask(request: HttpRequest) -> HttpResponse:


    #The request method is received from the function called fetchTask in the MainPage.svelte file
    if request.method == 'GET':
       #for task in TaskDetails.objects.filter(owner=request.user):
       #print(task.to_dict())


       #It fetches all the tasks details that are added by the user who is currently logged in and converted it to a JSON format.
       task_list = [
            task.to_dict()
            for task in TaskDetails.objects.filter(owner=request.user)
       ]

       #The JSON formatted task details are returned so that it can be accessed by the fetchTask function.
       return JsonResponse({

             'taskDetail':task_list

       })

#This function is used to update the task details in the database
@csrf_exempt
def UpdateTask(request: HttpRequest) -> HttpResponse:
    #The request method is received by the handleSubmit function in the TaskDetail.svelte file.
    #If it's POST http method, the updated task details for the specific task id will be saved to the database.
    if request.method == "POST":
         taskdetail = TaskDetails.objects.get(owner=request.user, id=request.POST['id'])
         taskdetail.name = request.POST['name']
         taskdetail.date = request.POST['date']
         taskdetail.startTime = request.POST['startTime']
         taskdetail.amountOfTime = request.POST['amountOfTime']
         taskdetail.descriptionOfTheTask = request.POST['descriptionOfTheTask']
         taskdetail.owner = request.user

         taskdetail.image = request.FILES['image']

         taskdetail.save()

         #The function will return the updated task details for the specific task id in a JSON format.
         #This is done by calling the to_dict() method that is implemented in the TaskDetails class in the models.py file
         return JsonResponse({

                'update_task':[
                       taskdetail.to_dict()
                ]

         })

#This function is used to delete the task details in the database
@csrf_exempt
def DeleteTask(request: HttpRequest) -> HttpResponse:
    #The request method is received from the handleDelete function that is implemented in the MainPage.svelte file.
    #If the http request method is POST, then the task details for a specific task id will be deleted from the database
    #and it will be disconnect from the user table.
    if request.method == 'POST':
         delete = json.loads(request.body)
         print(delete)
         deletedTask = TaskDetails.objects.get(owner=request.user, id=delete['task_id']) #This is where the deleted task details is saved in order to returned as a JSON format.
         print(deletedTask)
         taskDetail = TaskDetails.objects.get(owner=request.user, id=delete['task_id'])
         taskDetail.delete() #This is where the task details for the specific task id will be removed from the database.

         #The deleted task details will be returned in a JSON format, for the handleDelete function to be accessed in the MainPage.svelte file.
         return JsonResponse({

                'delete_task-detail':[
                    deletedTask.to_dict()
                ]

         })

    #If the request method received is not a POST http request, then no task details will be deleted.
    return JsonResponse({
              'delete_task-detail':[

               "The task detail cannot be deleted"

              ]
    })

#This function is used to store the amount of calorie for the food item that the user has typed in the calorie tracker form in the database.
@csrf_exempt
def CalorieTracker(request: HttpRequest) -> HttpResponse:



      #The request method is received from the javascript function calorieTracker which is implemented in the CalorieTracker.svelte file.
      #If the http request method is POST, then the calorie consumption details are saved in the database.
      #The owner field will allow the database to remember which user posted the calorie consumption detail.
      if request.method=="POST":
         calorietracker = CalorieDetail.objects.create(
             amountOfCalories = request.POST['listoffooditems'],
             currentDate = request.POST['dateinserted'],
             owner = request.user
         )

         calorietracker.save()


         #The calorie consumption will be returned in a JSON format for the corresponding function to access it.
         return JsonResponse({

              'calorie_detail':[

                   calorietracker.to_dict()

              ]

         })

      #If the response method is not POST, the the calorie consumption is not store in the database.
      return JsonResponse({
         'calorie_detail':[

               "The calories details are not added yet"

         ]
      })


#This function is used to fetch the user's calorie consumption history from the database.
@csrf_exempt
def CalorieDetailRetrieved(request:HttpRequest)->HttpResponse:



      #The request method is received by the javascript function called handleSubmit in the calorieHistory.svelte file.
      #If the http request method is GET, the all the calorie consumption that belongs to the log in user are fetched from the database.
      if request.method=="GET":



       #The calorie consumption details will be returned in a JSON format using the to_dict() function that is implemented in the CalorieDetail class in the models.py file, for the handleSubmit function to access it.
       return JsonResponse({

               'calorie_detail_retrieved':[
                  caloriedetail.to_dict()
                  for caloriedetail in CalorieDetail.objects.filter(owner=request.user)    #This is where the calorie intake details are fetched, by filtering out which details belongs to the current logged in user in the database.
               ]

       })

# Create your views here.
# class FilmListAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmDetailAPIView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer