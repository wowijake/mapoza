from django.shortcuts import render, redirect
from .models import Job
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login 
from django.contrib import messages


def home_page(request):
    return render(request, 'jobs/index.html')


def jobs_page(request):
    jobs = Job.objects.all().order_by('-date_created')
    context = { 'jobs': jobs }

    return render(request, 'jobs/jobs.html', context)

def about_page(request):
    context = { 'title': 'About Us' }
    return render(request, 'jobs/about.html', context)


def signup_page(request):
    ##form = UserCreationForm()
   ## return render(request, 'jobs/signup.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login.html')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'jobs/signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})
