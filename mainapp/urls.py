from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('', index, name="index"),
]