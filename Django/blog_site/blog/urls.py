from django.urls import path
from . import views

urlpatterns = [
		path("",views.index, name="index"),
		path("posts/",views.posts, name="posts_page"),
		path("posts/<slug:slug>", views.post_details, name="post_detail_page"),
	]