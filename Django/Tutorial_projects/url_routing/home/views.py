from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
# Create your views here.
def index(request):
	return HttpResponse("<h1>Apps' index page </h1>")
def january(request):
	return HttpResponse(" <a href='/home'><h1>January</h1></a><br>hello")
def months(request, month):
	text=None
	if month=="january":
		text="January"
	elif month=="february":
		text="february"
	else:
		text="its month"
		return Http404()
	return HttpResponse("<h1>"+text+"</h1>")