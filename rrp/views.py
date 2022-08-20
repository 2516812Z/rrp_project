from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import *
from django.contrib.auth.models import User
from rrp.forms import UserForm, UserProfileForm
from rrp.models import Users, Ransomware, Asset, RiskLevelAssessment, Event, Information
from django.utils import timezone


def register(request):
    registered = False
    reg_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(User.objects.filter(username=username)) < 1:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            users = Users.objects.create(user=user)
            if 'file' in request.FILES:
                users.picture = request.FILES['file']
            users.save()
            registered = True
        else:
            reg_message = "Username has already been registered!"
            print(reg_message)

    return render(request, 'register.html', {'registered': registered,
                                             'reg_message': reg_message})

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
    user_cirt = Users.objects.filter(cirt=True)
    messages = Information.objects.filter()
    if userinfo.position == 'admin':
        return render(request, 'indexAdmin.html', {'picture': userinfo.picture,
                                                   'cirts': user_cirt,
                                                   'messages': messages})
    return render(request, 'index.html', {'picture': userinfo.picture,
                                          'cirts': user_cirt,
                                          'messages': messages})

@login_required
def index_info(request, info_id):
    user = request.user
    userinfo = Users.objects.get(user=user)
    meg = Information.objects.get(id=info_id)
    if userinfo.position == 'admin':
        return render(request, 'infoAdmin.html', {'picture': userinfo.picture,
                                                   'meg': meg})
    return render(request, 'info.html', {'picture': userinfo.picture,
                                          'meg': meg})

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

        currentProcess = "Req"
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
    sub_action = request.POST.get('sub_action')
    repCount = len(event.reporters.all())
    if request.method == 'POST':
        if event.currentProcess == 'D&A' and sub_action == 'D&A':
            rName = request.POST.get('ransomwareName')
            rType = request.POST.get('ransomwareType')
            rAmount = request.POST.get('ransomAmount')
            duration = request.POST.get('duration')
            isKnown = request.POST.get('isKnown')
            reType = request.POST.get('recoveryType')
            reTime = request.POST.get('recoveryTime')
            reInfo = request.POST.get('recoveryInfo')
            event.ransomwareName = rName
            event.ransomwareType = rType
            event.ransomAmount = rAmount
            event.duration = duration
            event.isKnown = isKnown
            event.recoveryType = reType
            event.recoveryTime = reTime
            event.recoveryInfo = reInfo
            event.save()
        elif event.currentProcess == 'D&A' and sub_action == 'NEXT':
            event.currentProcess = "Report"
            event.save()
            repCount = len(event.reporters.all())
        elif event.currentProcess == 'Report' and sub_action == 'Report':
            event.reporters.clear()
            for rep in Users.objects.filter():
                if rep.reporter and request.POST.get(rep.user.username):
                    u = User.objects.get(username=rep.user.username)
                    event.reporters.add(u)
            event.save()
            repCount = len(event.reporters.all())
        elif event.currentProcess == 'Report' and sub_action == 'NEXT':
            event.currentProcess = "Recovery"
            event.save()
        elif event.currentProcess == 'Recovery' and sub_action == 'Recovery':
            recType = request.POST.get('recoveryType')
            recTime = request.POST.get('recoveryTime')
            recInfo = request.POST.get('recoveryInfo')
            handler = request.POST.get('handler')
            event.recoveryType = recType
            event.recoveryTime = recTime
            event.recoveryInfo = recInfo
            event.handler = handler
            event.save()
        elif event.currentProcess == 'Recovery' and sub_action == 'NEXT':
            event.currentProcess = "LL"
            event.save()
        elif event.currentProcess == 'LL' and sub_action == 'LL':
            record = request.POST.get('records')
            event.records = record
            event.save()
        elif event.currentProcess == 'LL' and sub_action == 'NEXT':
            event.currentProcess = "Completed"
            event.save()
        else:
            event.save()

    # Redirect to diffent web based on currentProcess
    if event.requestUser == userinfo or userinfo.position == 'admin':
        if userinfo.position == 'admin':
            if event.currentProcess == "D&A":
                return render(request, 'eventDAAdmin.html', {'picture': userinfo.picture,
                                                             'event': event})
            elif event.currentProcess == "Report":
                return render(request, 'eventReportAdmin.html', {'picture': userinfo.picture,
                                                                 'event': event,
                                                                 'repCount': repCount,
                                                                 'reporters': event.reporters.all()})
            elif event.currentProcess == "Recovery":
                return render(request, 'eventRecoveryAdmin.html', {'picture': userinfo.picture,
                                                                   'event': event,
                                                                   'repCount': repCount,
                                                                   'reporters': event.reporters.all()})
            elif event.currentProcess == "LL":
                return render(request, 'eventLLAdmin.html', {'picture': userinfo.picture,
                                                             'event': event,
                                                             'repCount': repCount,
                                                             'reporters': event.reporters.all()})
            elif event.currentProcess == "Completed":
                return render(request, 'eventCompletedAdmin.html', {'picture': userinfo.picture,
                                                             'event': event,
                                                             'repCount': repCount,
                                                             'reporters': event.reporters.all()})
            else:
                return redirect('/')
        if event.currentProcess == "D&A":
            return render(request, 'eventDA.html', {'picture': userinfo.picture,
                                                    'event': event})
        elif event.currentProcess == "Report":
            return render(request, 'eventReport.html', {'picture': userinfo.picture,
                                                        'event': event,
                                                        'repCount': repCount,
                                                        'reporters': event.reporters.all()})
        elif event.currentProcess == "Recovery":
            return render(request, 'eventRecovery.html', {'picture': userinfo.picture,
                                                          'event': event,
                                                          'repCount': repCount,
                                                          'reporters': event.reporters.all()})
        elif event.currentProcess == "LL":
            return render(request, 'eventLL.html', {'picture': userinfo.picture,
                                                    'event': event,
                                                    'repCount': repCount,
                                                    'reporters': event.reporters.all()})
        elif event.currentProcess == "Completed":
            return render(request, 'eventCompleted.html', {'picture': userinfo.picture,
                                                           'event': event,
                                                           'repCount': repCount,
                                                           'reporters': event.reporters.all()})
        else:
            return redirect('/')
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
    action = request.POST.get('sub_action')
    event_id = request.POST.get('sub_id')
    event = Event.objects.get(id=event_id)
    reporters = Users.objects.filter(reporter=True)
    if userinfo.position == 'admin':
        return render(request, 'settingsTable.html', {'picture': userinfo.picture,
                                                      'action': action,
                                                      'event': event,
                                                      'reporters': reporters})
    else:
        return redirect('/')


