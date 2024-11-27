from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Availability, Company
from .forms import AvailabilityForm, CustomUserCreationForm, CompanyRegistrationForm
import json 
from datetime import date
from django.contrib import messages
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.views import LoginView



def home(request):
    return render(request, 'index.html')

@login_required
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

@login_required
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

@login_required
def register_choice(request):
    # Function that Chooses between an existing cmopany and new company
    if request.method == 'POST':
        choice = request.POST.get('registration_choice')
        if choice == 'existing':
            return redirect('register_existing_company')
        elif choice == 'new':
            return redirect('company_registration')
    return render(request, 'register_choice.html')

@login_required
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


@login_required
def fill_options(request):
    if request.method == 'POST':
        tutor_name = request.POST.get('tutor_name')
        times = json.loads(request.POST.get('times'))  # Expecting a list of time slots
        recurring = request.POST.get('recurring')
        preferences = request.POST.get('preferences')

        # Create or get subject instances
        subject_instances = []


        # Save each time slot as an Availability object
        for time_slot in times:
            date_str, time_range = time_slot.split(' ')
            start_time, end_time = time_range.split(' - ')
            availability = Availability.objects.create(
                user=request.user,
                date=date_str,  # Using `date_str` here
                start_time=start_time,
                end_time=end_time,
                recurring=recurring,
                preferences=preferences
            )
            availability.subjects.set(subject_instances)

        return redirect('success_page')  # Replace with the desired success page

    else:
        today = date.today().isoformat()  # `date` here now refers to the `datetime.date` module
        return render(request, 'fill_options.html', {'today': today})

@login_required
def account(request):
    user = request.user

    # Get the user's availability if they're a tutor
    availability = Availability.objects.filter(user=user).order_by('date', 'start_time')

    # If the user is linked to a company, fetch company details
    company = None
    if hasattr(user, 'company'):
        company = user.company

    # Get reservations for clients
    reservations = None
    if hasattr(user, 'reservations'):  # Assuming a related_name='reservations' in your Reservation model
        reservations = user.reservations.all().order_by('date', 'start_time')

    context = {
        'user': user,
        'availability': availability,
        'company': company,
        'reservations': reservations,  # Pass reservations to the template
    }
    return render(request, 'account.html', context)

@login_required
def logout_view(request):
    logout(request)
    # Optionally, display a message or redirect the user after logging out
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')  # Redirect to the homepage or another page


class CustomLoginView(LoginView):
    template_name = 'login.html'


def profile_picture_context(request):
    profile_pic_url = None
    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(user=request.user, provider='google')
            profile_pic_url = social_account.extra_data.get('picture')  # 'picture' is the key for Google profile picture
        except SocialAccount.DoesNotExist:
            pass
    return {'profile_pic_url': profile_pic_url}
    