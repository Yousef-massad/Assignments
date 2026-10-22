from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    path('add' , views.add_course),
    path('remove/<int:id>' , views.remove_id),
    path('destroy/<int:id>' , views.remove),
]