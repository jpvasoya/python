from django.shortcuts import render
from django.http import HttpResponse
from .form import character_info

# Create your views here.
def index(request):
	context={}
	form=character_info(request.POST or None)
	context['form']=form
	return render(request,"movies/index.html",context)
def form_info(request):
	return HttpResponse(print(request.POST))
#	if slug!='admin':
#		return render(request,"movies/movies.html")

