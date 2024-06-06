from django.contrib import admin
from .models import Job, JobType


admin.site.register([Job,JobType])
