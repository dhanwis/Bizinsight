from django.urls import path
from bizapp.views import *
urlpatterns = [
    
     path('',home,name="homepage"),
     path('contact/',contact,name="contactpage"),
     path('about/',about,name="aboutpage"),
     path('service/',service,name="servicepage"),
     path('blog/',blog,name="blog")
     
]