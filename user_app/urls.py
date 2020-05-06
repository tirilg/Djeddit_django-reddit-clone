from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path("", views.login, name="login"), 
    path("signup/", views.signup, name="signup"), 
    path("login/", views.login, name="login"), 
]