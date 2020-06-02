import django_rq
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from reddit_app.models import Post
from .models import PasswordReset
from . messaging import password_req_email;


def signup(request):
    context = {}

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('reddit_app:index'))

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



def login(request):
    context = {}

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('reddit_app:index'))

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password= request.POST["password"])

        if user: 
            dj_login(request, user)
            return HttpResponseRedirect(reverse("reddit_app:index"))
        else: 
            context = {"error": "Invalid username or password combination"}
    
    return render(request, "user_app/login.html", context)

@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('user_app:login'))


@login_required
def settings(request):
    context = {}
    user = request.user
    context={"user": user}

    return render(request, "user_app/settings.html", context)


@login_required
def delete(request):
    context = {}

    if request.method == "POST":
        password = request.POST['password']
        if request.user.check_password(password):
            if request.POST['confirm_deletion'] == "DELETE":
                if user:
                    print(f"deleting user {user}")
                    user.delete()
                    return HttpResponseRedirect(reverse('reddit_app:index'))
                else:
                    context = {"del_message": "Deletion failed"}
            else: 
                context = {"del_message": "you need to write DELETE"}
        else: 
            context = {"del_message": "wrong password"}

    return render(request, 'user_app/settings.html', context)

@login_required
def update_password(request):
    context = {}

    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        new_password_confirm = request.POST['new_password_confirm']

        if request.user.check_password(old_password):
            if new_password == new_password_confirm:
                user = get_object_or_404(User, username=request.user.username)
                user.set_password(new_password)
                user.save()
                context = {"pass_message": "Password changed"}

                return HttpResponseRedirect(reverse('user_app:login'))
            else:
                context = {"pass_message": "Passwords do not match"}
        else:
            context = {"pass_message": "Wrong password"}

    return render(request, 'user_app/settings.html', context)


def request_reset_password(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        is_email_valid = User.objects.filter(email=email).exists()
    
        if is_email_valid:
            password_reset_request = PasswordReset()
            password_reset_request.email = email
            password_reset_request.save()

            django_rq.enqueue(password_req_email, {
                'reset_url': request.build_absolute_uri(reverse('user_app:reset_password')) + "?token=" + password_reset_request.token,
                'email': password_reset_request.email,
            })

            context = {"email_sent": True}

        else:
            context = {'message': 'This email does not exist in the database'}
    
    return render(request, 'user_app/request-reset-password.html', context)


def reset_password(request):
    context = {}
    token = request.GET.get('token', None)

    if request.method == 'POST':
        if token:
            email = request.POST['password-reset-email']
            password = request.POST['password-reset-password']
            password_confirm = request.POST['password-reset-password-confirm']

            if password == password_confirm: 
                is_token_valid = PasswordReset.objects.filter(token=token, active=True).exists()
                is_user_valid = User.objects.filter(email=email).exists()

                if is_token_valid and is_user_valid:
                    token = PasswordReset.objects.get(token=token)
                    token.active = False
                    token.save()

                    user = User.objects.get(email=email)
                    user.set_password(password)
                    user.save()

                    return redirect('user_app:login')

                else:
                    context = { 'message': 'token or email is invalid' }
            else:
                context = { 'message': 'passwords do not match' }
        else:
            context = {'message': 'no token provided'}

    return render(request, 'user_app/reset-password.html', context)
