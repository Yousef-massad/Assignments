from django.shortcuts import path
from . import views

urlpatterns = [
    path('' , views.index)
]