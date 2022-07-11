from django.urls import path
from .import views

app_name = 'edu'

urlpatterns = [
    path('skill/',views.skill, name='skill')
]