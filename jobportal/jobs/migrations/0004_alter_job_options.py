# Generated by Django 5.0.6 on 2024-07-24 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-date_created']},
        ),
    ]
