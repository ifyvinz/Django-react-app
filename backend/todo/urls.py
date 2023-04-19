from django.urls import path
from . import views
#need to be able to upload images
from django.conf.urls.static import static
from django.conf import settings

#from rest_framework_simplejwt.views import (
   # TokenObtainPairView,
    #TokenRefreshView,
#)

urlpatterns = [
    path("", views.index, name="index"),
    path("api/register", views.register, name="register"),
    path("api/login", views.login_view, name="login"),
    path("api/logout", views.logout_view, name="logout"),
    
    path("api/newPost", views.newPost, name="newPost"),
    #path("api/get_csrf_token", views.get_csrf_token, name="get_csrf_token"),
    path("api/todoList", views.todoList, name="todoList"),
    path("api/<int:id>/deleteTask", views.deleteTask, name="deleteTask"),
    path("api/<int:id>/setCompleted", views.setCompleted, name="setCompleted"),
    path("api/completed_task", views.completed_task, name="completed_task"),
    #path('api/authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('api/authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)