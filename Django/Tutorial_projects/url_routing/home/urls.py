from django.urls import path
from . import views
urlpatterns=[
		path("",views.index),
		path("january",views.january),
		path("<month>",views.months)
]