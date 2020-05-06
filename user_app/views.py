from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import authenticate, update_session_auth_hash, login as dj_login, logout as dj_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from reddit_app.models import Post

### Sign up 
def signup(request):
    context = {}

    if request.method == "POST":
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password: 
            if User.objects.create_user(username, email, password):
                return HttpResponseRedirect(reverse('user_app:login'))
            else:
                context = {
                    'error': 'Could not create user account - Please try again.'
                }
        else:
            context = {
                'error': 'Passwords did not match - Please try again.'
            }
    return render(request, 'user_app/signup.html', context)


### Log in
def login(request):
    context = {}

    #login request
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password= request.POST["password"])

        if user: 
            #user login success
            dj_login(request, user)
            return HttpResponseRedirect(reverse("reddit_app:index"))
        else: 
            #user login failed
            context = {"error_message": "Invalid username or password combination"}
    
    return render(request, "user_app/login.html", context)


