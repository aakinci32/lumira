"""
URL configuration for lumira project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from lumira import views
from django.conf import settings
from django.conf.urls.static import static
from lumira.views import CustomLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.add_availability, name='add_availability'),
    path('register/', views.register, name='register'),
    path('register_new_company/', views.register_choice, name='register_choice'),
    path('register_existing_company/', views.register_existing_company, name='register_existing_company'),
    path('company_registration/', views.company_registration, name='company_registration'),
    path('fill_options', views.fill_options, name='fill_options'), 
    path('account', views.account, name='account'), 
    path('logout/', views.logout_view, name='logout'),  # Add this line
    path('login/', CustomLoginView.as_view(), name='login'),
    
    
    
]

# Serve media files during development
if settings.DEBUG:  # Only in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('allauth.urls')),  # Adds the OAuth routes
]