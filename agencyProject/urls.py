"""agencyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from agencyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.CusTokenView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', views.UserCreateView.as_view()),

    path('user/', views.UserGetView.as_view()),
    path('user/<int:id>/', views.UserGetView.as_view()),

    path('pack/', views.PackAdminView.as_view()),
    path('pack/list/', views.PackGetView.as_view()),
    path('pack/list/<int:id>/', views.PackGetView.as_view()),
    path('pack/<int:id>/', views.PackAdminView.as_view()),

    path('purchase/', views.PurchaseCreateView.as_view()),
    path('purchase/list/', views.PurchaseGetView.as_view()),
    path('purchase/list/<int:userid>/', views.PurchaseGetView.as_view()),
    path('purchase/<int:id>/', views.PurchaseGetView.as_view()),
]
