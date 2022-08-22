"""rrp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rrp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_login, name='login'),
    path('main/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('event_request/', views.event_request, name='event_request'),
    path('event_check/', views.event_check, name='event_check'),
    path('event_info/<event_id>', views.event_info, name='event_info'),
    path('event_list/', views.event_list, name='event_list'),
    path('asset_value/', views.asset_value, name='asset_value'),
    path('ransomware_type/', views.ransomware_type, name='ransomware_type'),
    path('role/', views.role, name='role'),
    path('risk_level_assessment', views.risk_level_assessment, name='risk_level_assessment'),
    path('settings_table/', views.settings_table, name='settings_table'),
    path('info/<info_id>', views.index_info, name='index_info')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
