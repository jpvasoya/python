from django.urls import path
from . import views
urlpatterns=[
	path("", views.index, name="index"),
	path("form",views.form_info,name="form")
	#path("<slug:slug>", views.list, name="list"),
]