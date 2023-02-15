from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Coordinator,Proposal,Event,SubCoordinator,SubEvent,Volunteer,Participant,Payment,Notification,Memories
from .forms import VolunteerForm,ParticipantForm,CustomUserForm


def home(request):
    return render(request,'home/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'eventbrite/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('dashboard')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            print("Registration Successfull!!!")
            return redirect('dashboard')
    else:
        form = CustomUserForm()
    return render(request, 'register/register.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    return render(request,'eventbrite/dashboard.html')

def events(request):
    events=Event.objects.all()
    context={
        'events':events
    }
    return render(request,'eventbrite/events.html',context)

def event_data(request,pid):
    event=Event.objects.get(pk=pid)
    subevents=SubEvent.objects.all().filter(event=event.id)
    context={
        'event':event,
        'subevents':subevents,
    }
    return render(request,'eventbrite/event_data.html',context)

def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = VolunteerForm()
    return render(request, 'eventbrite/volunteer.html', {'form': form})

def participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ParticipantForm()
    return render(request, 'eventbrite/participant.html', {'form': form})

