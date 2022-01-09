from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
days={
"monday":"Its Monday lets eat agg because monday is eggday!!",
"tuesday":"Lets Work out on Tuesday....",
"wednesday":"Read Story book on wednesday",
"thursday":"Date with Girlfriend and enjoy it..",
"friday":"watch movies on cinema house..",
"saturday":"Go to the temple.",
"sunday":"sunday funday🤣🤣it is weakend day",
}
# Create your views here.
def index(request):
	days1=list(days.keys())
	listi=""
	for day in days1:
		item=day.capitalize()
		path=reverse("day", args=[day])
		listi+=f"<li><a href='{path}'>{item}</li>"
	return HttpResponse(f"<ul><h1>{listi}</h1></ul>")
def weakly_num(request,day):
	try:
		list1=list(days.keys())
		text=list1[day-1]
		return HttpResponseRedirect(text)
	except:
		return HttpResponseNotFound("invalid number")
	#days_key=list(days.keys())
	#redirect=reverse("number",args=days[day])
def weakly_challenge(request, day):
		#dict=list(days.keys())
		try:
			text=days[day]
			path=reverse("index")
			return HttpResponse(f"<h1>{text}</h1><br><a href='{path}'>Back</a>")
		except:
			path=reverse("index")
			return HttpResponseNotFound(f"<h1>this day not supported!</h1><br><a href='{path}'>Back</a>")
