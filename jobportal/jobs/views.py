from django.shortcuts import render, redirect
from .models import Job, JobType
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.db.models import Q


def home_page(request):
    return render(request, 'jobs/index.html')


def jobs_page(request):
    job_types = JobType.objects.all().order_by('type_name')
    # filtering jobs on job schedule
    if 'filter' in request.GET:
        filter = request.GET.get('filter')
        jobs = Job.objects.filter(job_type__type_name=filter).order_by('-date_created')
        context = { 'jobs': jobs, 'job_types': job_types,  'colors': ['info', 'warning', 'danger',] }
    # search for jobs on keywords
    elif 'query' in request.GET:
        query = request.GET.get('query')
        jobs = Job.objects.filter(Q(title__icontains=query) | Q(company_name__icontains=query) | Q(location__icontains=query) | Q(description__icontains=query) | Q(job_type__type_name__icontains=query))
        context = { 'jobs': jobs, 'job_types': job_types,  'colors': ['info', 'warning', 'danger', 'success'] }
    else:
        jobs = Job.objects.all().order_by('-date_created')
        context = { 'jobs': jobs, 'job_types': job_types,  'colors': ['info', 'warning', 'danger', 'primary'] }

    return render(request, 'jobs/jobs.html', context)

def job_detail_page(request, pk):
    job = Job.objects.get(pk=pk)
    context = { 'job': job, 'colors': ['info', 'warning', 'danger', 'primary'], }
    return render(request, 'jobs/job_detail.html', context)

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
            return redirect('login-page')  # Redirect to login page after successful signup
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
                return redirect('jobs-page')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('login-page')
