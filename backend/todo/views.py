from django.shortcuts import get_object_or_404, render
import json
from rest_framework.decorators import api_view
#from django.views.decorators.csrf import ensure_csrf_cookie
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from .models import Todo, User, Completed
from .serializers import TodoSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#import rest_framework_simplejwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken



#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
#@ensure_csrf_cookie
#def get_csrf_token(request):
    #return JsonResponse({'csrfToken': request.COOKIES['csrftoken']})


#class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   # @classmethod
   # def get_token(cls, user):
    #    #token = super().get_token(user)

        # Add custom claims
        #token['username'] = user.username
        # ...

       # return token


#class MyTokenObtainPairView(TokenObtainPairView):
    #serializer_class = MyTokenObtainPairSerializer


# Add the following import line
from django.contrib.auth import get_user_model

# Replace all references to User with get_user_model() such as...
#user = get_user_model().objects.get(pk=uid)
# instead of  user = User.objects.get(pk=uid)
# or
#queryset = get_user_model().objects.all()
# instead of queryset = User.objects.all()
# etc...


def index(request):
    todo = Todo.objects.all()
    #content =  pagination(request, posts)
    return render(request, "todo/index.html", {
        "too": todo,
        
    })

@api_view(['GET'])
def todoList(request):
    todoObj = Todo.objects.all()
    serialize = TodoSerializer(todoObj, many = True)

    response = {
        'todoList': serialize.data
    }
    return JsonResponse(response, status = 200)
@api_view(['POST'])
def newPost(request):
    if request.method != "POST":
        return render(request, "todo/index.html")
    #user = get_user_model().objects.get(pk=uid)
    #user = User.objects.get(username = "ifyvinz")
    user = get_user_model().objects.get(username = "ifyvinz")
    print(user)
    #data = json.loads(request.body)
        #get the body of post
    #title = data.get("title", "")
    #description = data.get("description", "")
    title = request.POST.get("title")
    description = request.POST.get("description")
    
        #save into database
    if len(title) > 0 or len(description) > 0:
        todoObj = Todo(author = user, title = title, description = description)
        todoObj.save()
        #serialize
        allTask= Todo.objects.all()
        serialize = TodoSerializer(allTask, many = True)

        #send back the post in json fomart
        #index(request)
        response ={
            'task': serialize.data,
            'message': "successfully posted."
        }
        return JsonResponse(response, status=201)
    #return JsonResponse({"message": "failed"}, status = 400)

@api_view(['DELETE'])
def deleteTask(request, id):
    if request.method == "DELETE":
        #task = Todo.objects.get(pk=id)
        #data= json.load(request.body)
        #id = data.get("id", "")
        task = get_object_or_404(Todo, pk=id)
        task.delete()
        
        allTask= Todo.objects.all()
        serialize = TodoSerializer(allTask, many = True)

        #send back the post in json fomart
        #index(request)
        #{"message": "Taks deleted"}
        response ={
            'tasks': serialize.data,
            'message': "successfully posted."
        }
        return JsonResponse(response, status = 200)
    return JsonResponse({"message": "select a task to be deleted"}, status = 201)

@api_view(['PUT'])
def setCompleted(request, id):
    if request.method == "PUT":
        task = Todo.objects.get(pk=id)
        task.completed = not task.completed
        task.save()

        allTask= Todo.objects.all()
        serialize = TodoSerializer(allTask, many = True)

        #send back the post in json fomart
        #index(request)
        response ={
            'tasks': serialize.data,
            'message': "successfully posted."
        }
        return JsonResponse(response, status=200)
    return JsonResponse({"message": "Check completed"}, status = 201)