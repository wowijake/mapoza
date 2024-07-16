from django.shortcuts import render
from .models import Job
from django.contrib.auth.forms import UserCreationForm


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
    form = UserCreationForm
    return render(request, 
                    'jobs/signup.html',
  context={"form":form})
