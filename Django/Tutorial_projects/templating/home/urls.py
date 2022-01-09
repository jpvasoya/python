from django.urls import path
from . import views
urlpatterns=[
	path("", views.index, name="index"),
	path("<int:day>", views.weakly_num,name="number"),
	path("<str:day>",views.weakly_challenge, name="day"),
]