from django.db import models
from ckeditor.fields import RichTextField


class JobType(models.Model):
    type_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.type_name


class Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    company_name = models.CharField(max_length=150, null=False)
    location = models.CharField(max_length=255, null=False)
    job_type = models.ManyToManyField(JobType)
    description = RichTextField(null=False, blank=True, help_text='Job description and requirements')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title} - {self.company_name}'
