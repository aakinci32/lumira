from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Availability
from .forms import AvailabilityForm, CustomUserCreationForm
import json 
from datetime import date


def home(request):
    return render(request, 'index.html')


def add_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = request.user
            availability.save()
            return redirect('view_availability')
    else:
        form = AvailabilityForm()
    return render(request, 'add_availability.html', {'form': form, 'today': date.today().isoformat()})


def register(request):
    # When the User Clicks Register from the Home Page This Functionality comes up
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

