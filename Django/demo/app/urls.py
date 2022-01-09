from django.urls import path
from . import views
urlpatterns=[
	path("",views.index, name="index"),
	path("posts",views.all_post, name="allpost"),
	path("posts/<slug:slug>",views.post_details, name="post_details")
]