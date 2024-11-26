from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Availability, Company
from .forms import AvailabilityForm, CustomUserCreationForm, CompanyRegistrationForm
import json 
from datetime import date
from django.contrib import messages



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

def company_registration(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Company registration successful!')
            return redirect('fill_options')
    else:
        form = CompanyRegistrationForm()

    return render(request, 'fill_options.html', {'form': form})

def register_choice(request):
    # Function that Chooses between an existing cmopany and new company
    if request.method == 'POST':
        choice = request.POST.get('registration_choice')
        if choice == 'existing':
            return redirect('register_existing_company')
        elif choice == 'new':
            return redirect('company_registration')
    return render(request, 'register_choice.html')

def register_existing_company(request):
    # 
    if request.method == 'POST':
        # Process user registration under the selected company
        company_id = request.POST.get('company')
        company = Company.objects.get(id=company_id)
        # TODO: Adjust this later
        return redirect('fill_options')  # TODO: Edit this when I have the add availability option 

    companies = Company.objects.all()
    return render(request, 'register_existing_company.html', {'companies': companies})


def fill_options(request):
    if request.method == 'POST':
        tutor_name = request.POST.get('tutor_name')
        times = json.loads(request.POST.get('times'))
        recurring = request.POST.get('recurring')
        subjects = request.POST.get('subjects')
        preferences = request.POST.get('preferences')

        # Save the availability and additional information
        for time in times:
            # Save each time slot along with tutor details in the database
            pass # TODO: Fill this in later when the database is alligned

        return redirect('success_page')  # Replace with the desired success page
    else:
        today = date.today().isoformat()
        return render(request, 'fill_options.html', {'today': today})

    

def account(request):
    user = request.user
    # Get the user's availability if they're a tutor
    availability = Availability.objects.filter(user=user).order_by('date', 'start_time')

    # If the user is linked to a company, fetch company details
    company = None
    if hasattr(user, 'company'):
        company = user.company

    context = {
        'user': user,
        'availability': availability,
        'company': company,
    }
    return render(request, 'account.html', context)
