from django.shortcuts import render
from .models import Job


def home_page(request):

    jobs = Job.objects.all().order_by('-date_created')
    context = { 'jobs': jobs }

    return render(request, 'jobs/index.html', context)


def about_page(request):
    return render(request, 'jobs/about.html')

