from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index1"),
    path('<int:month>',views.number),
    path('<str:month>',views.months,name="index")
]