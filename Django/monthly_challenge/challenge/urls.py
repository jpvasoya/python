from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index),
    path('<int:month>', views.number),
    path('<str:month>', views.months, name="index"),
    
]