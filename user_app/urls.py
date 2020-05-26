from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path("", views.login, name="login"), 
    path("signup/", views.signup, name="signup"), 
    path("login/", views.login, name="login"), 
    path("logout/", views.logout, name="logout"), 
    path("settings/", views.settings, name="settings"), 
    path("delete/", views.delete, name="delete"), 
    path("update-password/", views.update_password, name="update_password"), 
    path("request-reset-password/", views.request_reset_password, name="request_reset_password"), 
    path("reset-password/", views.reset_password, name="reset_password"), 
]