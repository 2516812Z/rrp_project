from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    # registered = False
    # if request.method == 'POST':
        # user_form = UserForm(request.POST)
        # profile_form = UserProfileForm(request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        #     user = user_form.save()
        #     user.set_password(user.password)
        #     user.save()
        #     profile = profile_form.save(commit=False)
        #     profile.user = user
        #
        #     if 'picture' in request.FILES:
        #         profile.picture = request.FILES['picture']
        #     profile.save()
        #     registered = True
        # else:
        #     print(user_form.errors, profile_form.errors)
    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileForm()
    # return render(request, 'register.html',
    #               context={'user_form': user_form,
    #                        'profile_form': profile_form,
    #                        'registered': registered})
    return render(request, 'register.html')

def login(request):
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
