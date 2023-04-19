from django.shortcuts import get_object_or_404, render
import json

#from django.views.decorators.csrf import ensure_csrf_cookie
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from .models import Todo, User, Completed
from .serializers import TodoSerializer, UserSerializer, CompletedSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication






# Create your views here.
#@ensure_csrf_cookie
#def get_csrf_token(request):
    #return JsonResponse({'csrfToken': request.COOKIES['csrftoken']})


#

# Add the following import line
from django.contrib.auth import get_user_model

# Replace all references to User with get_user_model() such as...
#user = get_user_model().objects.get(pk=uid)
# instead of  user = User.objects.get(pk=uid)
# or
#queryset = get_user_model().objects.all()
# instead of queryset = User.objects.all()
# etc...

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method != "POST":
       return JsonResponse({'errors': "Method not allowed."}, status=405)
    
    #load the json content
    data = json.loads(request.body)
    username = data.get("username", "")
    email = data.get("email", "")
    first_name = data.get("firstname", "")
    last_name = data.get("lastname", "")
    password = data.get("password", "")
    confirmation = data.get("confirm", "")

    # Ensure password matches confirmation
    if password != confirmation:
        print(password)
        print("-------------------------------")
        print(confirmation)
        return JsonResponse({
            "message": "Passwords must match."
        }, status = 403)

    # Attempt to create new user
    try:
        #user =  get_user_model().objects.create_user(username, password)
        #user =  User.objects.create_user(username, password)
        user = User.objects.create_user(username, email, password)
        #user.save()
        serializer = UserSerializer(user)
        print(last_name)
        print("-----")
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        print(user.last_name)
        token = Token.objects.create(user=user)
        print(token.key)
    except IntegrityError:
        return JsonResponse({
            "message": "Username already taken.",
            'username': username
        },status = 400)
    
    login(request, user)
    response = {
        'token': token.key, 
        'message': f"You now registred in Django. {username}.",
        'username': username
    }
    return JsonResponse(response, status = 200)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
     
    if request.method != "POST":
       return JsonResponse({'errors': "Method not allowed."}, status=405)
        
    #load the json content
    logout(request)
    data = json.loads(request.body)
    usern = data.get("username", "")
   # me = User.objects.get(username=usern)
    print( User.objects.get(username=usern).password)
    username = User.objects.get(username=usern).username
    password = data.get("password", "")
    
    print(username)
    print("-------------------")
    print(password)
    user = authenticate(request, username=username, password=password)
    print(user)
    # Check if authentication successful
    if user is not None:
         # User has logged in before, check if the token is still valid
        token = Token.objects.get(user=user)
        if token:
            # Token is still valid, return the existing token
            #token = Token.objects.get(user=user)
            #if token.is_valid():
                 #token = user.token
            login(request, user)
            response = {
                'token': token.key, 
                'message': f"You are already Logged in.. {username}.",
                 'username': username
                }
            return JsonResponse(response, status=201)
            #else:
                    # Token has expired, create a new one
                    #token = Token.objects.create(user=user)
                    #user.token = token
                    #user.save()
                    #return JsonResponse({'token': token.key, "message": f"Here is your new token {username}."}, status = 201)
        else:
                # User has never logged in before, create a new token
                token = Token.objects.create(user=user)
                #user.token = token
                #user.save()
                login(request, user)
                response = {
                'token': token.key, 
                'message': f"You are already Logged in.. {username}.",
                 'username': username
                }
                return JsonResponse(response, status=201)
    else:
            response = {'error': 'Invalid username or password'}
            return JsonResponse(response, status=401)
                    
                   
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])      
def logout_view(request):
    Token.objects.filter(user=request.user).delete()
    return JsonResponse({'message': 'User logged out successfully'})



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
    user = User.objects.get(username = "ifyvinz")
    #user = get_user_model().objects.get(username = "ifyvinz")
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def setCompleted(request, id):
    if request.method == "PUT":
        task = Todo.objects.get(pk=id)
        task.completed = not task.completed
        task.save()
        
        if task.completed:
            completeTask = Completed(completed_by= request.user, completed_task = task)
            completeTask.save()
        else:
            completeTask = Completed.objects.filter(completed_task = task)
            completeTask.delete()
        print("....")
        print(request.user)
        print("....")
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def completed_task(request):
    task_completed = Completed.objects.filter(completed_by=request.user)
    tasks = [task.completed_task for task in task_completed]

    serialize = TodoSerializer(tasks, many=True)

    response ={
        'tasks': serialize.data,
        'message': "All completed tasks."
    }
    return JsonResponse(response, status=200)
