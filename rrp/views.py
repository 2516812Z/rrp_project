from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import *
from django.contrib.auth.models import User
from rrp.forms import UserForm, UserProfileForm
from rrp.models import Users, Ransomware, Asset, RiskLevelAssessment, Event
from django.utils import timezone


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
    if userinfo.position == 'admin':
        return render(request, 'indexAdmin.html', {'picture': userinfo.picture})
    return render(request, 'index.html', {'picture': userinfo.picture})

@login_required
def userprofile(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    if userinfo.position == 'admin':
        return render(request, 'userprofileAdmin.html', {'picture': userinfo.picture})
    return render(request, 'userprofile.html', {'picture': userinfo.picture})

@login_required
def event_request(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    if request.method == 'POST':
        # Event Request
        requestTime = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")

        reqUser = request.POST.get('requestUser')
        re_user = User.objects.get(username=reqUser)
        requestUser = Users.objects.get(user=re_user)

        userAssetName = request.POST.get('assetName')
        try:
            userAsset = Asset.objects.get(assetName=userAssetName)
        except Asset.DoesNotExist:
            userAsset = None

        rName = request.POST.get('rName')
        try:
            ransomware = Ransomware.objects.get(ransomwareName=rName)
            ransomwarename = ransomware.ransomwareName
        except Ransomware.DoesNotExist:
            ransomware = None
            ransomwarename = None

        rType = request.POST.get('rType')
        rAmount = request.POST.get('rAmount')
        duration = request.POST.get('duration')
        desc = request.POST.get('desc')

        # Event Check & Analysis
        if ransomware != None:
            datalevel = userAsset.dataLevel
            ransomwareType = ransomware.ransomwareType
            riskLevel = RiskLevelAssessment.objects.get(dataLevel=datalevel, ransomwareType=ransomwareType).riskLevel
            isK = True
        else:
            riskLevel = "None"
            isK = False

        currentProcess = "C&A"
        event = Event.objects.create(requestTime=requestTime, requestUser=requestUser, userAsset=userAsset,
                                     ransomware=ransomware, ransomwareName=ransomwarename, ransomwareType=rType,
                                     ransomAmount=rAmount, duration=duration, description=desc, riskLevel=riskLevel,
                                     isKnown=isK, currentProcess=currentProcess)
        event.save()
        return redirect('/event_check')
    else:
        allassets = Asset.objects.filter()
        allransomwares = Ransomware.objects.filter()
        if userinfo.position == 'admin':
            return render(request, 'eventRequestAdmin.html', {'picture': userinfo.picture,
                                                              'allAssets': allassets,
                                                              'allRansomwares': allransomwares})
        return render(request, 'eventRequest.html', {'picture': userinfo.picture,
                                                     'allAssets': allassets,
                                                     'allRansomwares': allransomwares})

@login_required
def event_check(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    events = Event.objects.filter(requestUser=userinfo)
    if userinfo.position == 'admin':
        return render(request, 'eventCheckAdmin.html', {'picture': userinfo.picture,
                                                        'events': events})
    return render(request, 'eventCheck.html', {'picture': userinfo.picture,
                                               'events': events})

@login_required
def event_info(request, event_id):
    user = request.user
    userinfo = Users.objects.get(user=user)
    event = Event.objects.get(id=event_id)
    if (event.requestUser == userinfo or userinfo.position == 'admin'):
        if userinfo.position == 'admin':
            return render(request, 'eventInfoAdmin.html', {'picture': userinfo.picture,
                                                           'event': event})
        return render(request, 'eventInfo.html', {'picture': userinfo.picture,
                                                  'event': event})
    else:
        return redirect('/')


@login_required
def event_list(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    if userinfo.position == 'admin':
        events = Event.objects.filter()
    else:
        events = None
    return render(request, 'eventList.html', {'picture': userinfo.picture,
                                              'events': events})

@login_required
def asset_value(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    allassets = Asset.objects.filter()
    if userinfo.position == 'admin':
        return render(request, 'assetValue.html', {'picture': userinfo.picture,
                                                   'allAssets': allassets})
    else:
        return redirect('/')

@login_required
def ransomware_type(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    allransomwares = Ransomware.objects.filter()
    if userinfo.position == 'admin':
        return render(request, 'ransomwareType.html', {'picture': userinfo.picture,
                                                       'allRansomwares': allransomwares})
    else:
        return redirect('/')

@login_required
def role(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    allusers = Users.objects.filter()
    if userinfo.position == 'admin':
        return render(request, 'role.html', {'picture': userinfo.picture,
                                             'allUsers': allusers})
    else:
        return redirect('/')

@login_required
def risk_level_assessment(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    allassessments = RiskLevelAssessment.objects.filter()
    if userinfo.position == 'admin':
        return render(request, 'riskLevelAssessment.html', {'picture': userinfo.picture,
                                                            'allAssessments': allassessments})
    else:
        return redirect('/')

@login_required
def settings_table(request):
    user = request.user
    userinfo = Users.objects.get(user=user)
    if userinfo.position == 'admin':
        return render(request, 'settingsTable.html', {'picture': userinfo.picture})
    else:
        return redirect('/')


