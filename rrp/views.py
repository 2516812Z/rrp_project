from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import *
from rrp.forms import UserForm, UserProfileForm
from rrp.models import Users


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                print(user)
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'login.html', {
                'login_message': 'Enter the username and password incorrectly', })
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('login'))

@login_required
def index(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    return render(request, 'index.html', {'picture': userinfo.picture})

@login_required
def userprofile(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    return render(request, 'userprofile.html', {'picture': userinfo.picture})

@login_required
def event_request(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    return render(request, 'eventRequest.html', {'picture': userinfo.picture})

@login_required
def event_check(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    return render(request, 'eventCheck.html', {'picture': userinfo.picture})

@login_required
def event_info(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    return render(request, 'eventInfo.html', {'picture': userinfo.picture})


