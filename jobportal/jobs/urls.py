from django.urls import path
from .views import (
    home_page, 
    about_page, 
    jobs_page
)



urlpatterns = [
    path('', home_page, name='home-page'),
    path('about/', about_page, name='about-page'),
    path('jobs/', jobs_page, name='jobs-page'),
    path('signup/',views.signup,name="signup")
]




