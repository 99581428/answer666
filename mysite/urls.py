"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from cmdb import views
from mysite import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'reg/',views.register,name='register'),
    url(r'index/',views.index,name='index'),
    url(r'login/',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),
    url(r'search/',views.search, name='search'),
    url(r'answer/',views.answer, name='answer'),
    url(r'ajaxrg/',views.ajaxreg,name='ajaxreg'),
    url(r'admin/',admin.site.urls),
    url(r'captcha/',include('captcha.urls')),
    url(r'contactus/',views.contactus,name='contactus'),
    url(r'myanswers/',views.myanswers,name='myanswers'),
    url(r'myinformation/',views.myinformation,name='myinformation'),
    url(r'send_sms_view/', views.send_sms_view, name='send_sms_view'),
    url(r'^$',views.index),

]
