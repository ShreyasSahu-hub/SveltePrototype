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

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskSerializer

def SignUp(request: HttpRequest) -> HttpResponse:

    form = SignUpForm()

    if request.method == 'GET':
        return render(request, "protocolApplication/signup.html", {
            "form": form,
        })

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
             firstName = form.cleaned_data['firstName']
             lastName = form.cleaned_data['lastName']
             username = form.cleaned_data['username']
             email = form.cleaned_data['user_email']
             password = form.cleaned_data['password']
             password_confirm = form.cleaned_data['password_confirm']
             if password == password_confirm:
               try:
                 CreateUser = User.objects.create(firstName=firstName, lastName=lastName, username=username, user_email=email)
                 CreateUser.set_password(password)
                 CreateUser.save()
               except:
                     return HttpResponse("The username is already taken. Please type another username")

             user = auth.authenticate(firstName=firstName, lastName=lastName, username=username, user_email=email, password=password, password_confirm=password)
             if user is not None:
                 auth.login(request, user)
                 #return redirect('/login')
                 return redirect('/login')
             return HttpResponse("Password doesn't match")

def Login(request: HttpRequest) -> HttpResponse:

   form = LoginPage()

   if request.method == 'GET':
        return render(request, "protocolApplication/login.html", {
            "form": form,
        })

   if request.method == 'POST':
        form = LoginPage(request.POST)
        #PermissionChecker = User.objects.get()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            print("sfbsdfbsdtgn: " + str(user is not None))

            print("serfbsetfbsetbn" + str(request.user))

            UserObjectEmail = User.objects.filter(username=username).values("user_email")

            if user is not None:

                 auth.login(request, user)

                 return redirect('http://localhost:5173/mainpage')

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

@csrf_exempt
def AddTask(request:HttpRequest) -> HttpResponse:

        print(request.user)

        if request.method == 'POST':

           #console.log("srfbgsdzrfbhsdtfb")

           print("asrfbrsetn")

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

           return JsonResponse({

              'task_detail':[

                   taskdetail.to_dict()

              ]

           })

        return JsonResponse({
              'task_detail':[

               "The task details are not added yet"

              ]
         })

@csrf_exempt
def FetchTask(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
       #for task in TaskDetails.objects.filter(owner=request.user):
       #print(task.to_dict())

       task_list = [
            task.to_dict()
            for task in TaskDetails.objects.filter(owner=request.user)
       ]

       return JsonResponse({

             'taskDetail':task_list

       })

@csrf_exempt
def UpdateTask(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
         taskdetail = TaskDetails.objects.get(owner=request.user, id=request.POST['id'])
         taskdetail.name = request.POST['name']
         taskdetail.date = request.POST['date']
         taskdetail.startTime = request.POST['startTime']
         taskdetail.amountOfTime = request.POST['amountOfTime']
         taskdetail.descriptionOfTheTask = request.POST['descriptionOfTheTask']
         taskdetail.owner = request.user

         if request.FILES['image']!=None:

           taskdetail.image = request.FILES['image']

           taskdetail.save()

         else:

           taskdetail.save()

         return JsonResponse({

                'update_task':[
                       taskdetail.to_dict()
                ]

         })

@csrf_exempt
def DeleteTask(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
         delete = json.loads(request.body)
         print(delete)
         deletedTask = TaskDetails.objects.get(owner=request.user, id=delete['task_id'])
         print(deletedTask)
         taskDetail = TaskDetails.objects.get(owner=request.user, id=delete['task_id'])
         taskDetail.delete()

         return JsonResponse({

                'delete_task-detail':[
                    deletedTask.to_dict()
                ]

         })

    return JsonResponse({
              'delete_task-detail':[

               "The task detail cannot be deleted"

              ]
    })

@csrf_exempt
def CalorieTracker(request: HttpRequest) -> HttpResponse:
      if request.method=="POST":
         calorietracker = CalorieDetail.objects.create(
             amountOfCalories = request.POST['listoffooditems'],
             currentDate = request.POST['dateinserted'],
             owner = request.user
         )

         calorietracker.save()

         return JsonResponse({

              'calorie_detail':[

                   calorietracker.to_dict()

              ]

         })

      return JsonResponse({
         'calorie_detail':[

               "The calories details are not added yet"

         ]
      })

@csrf_exempt
def CalorieDetailRetrieved(request:HttpRequest)->HttpResponse:
      if request.method=="GET":

       return JsonResponse({

               'calorie_detail_retrieved':[
                  caloriedetail.to_dict()
                  for caloriedetail in CalorieDetail.objects.filter(owner=request.user)
               ]

       })

# Create your views here.
# class FilmListAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmDetailAPIView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer