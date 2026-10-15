from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('add/', views.add),
  path('remove/<int:id>/', views.remove),
  path('update/<int:id>/', views.update),
]