from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse

# Create your views here.
#def index(request):
#	return render(request,"index.html")
dict={
'january':'its january',
'february':'its february',
'march':"its march",
'april':"its april",
'may':"my bad day",
'june':"its june",
'july':"its july",
'august':"its august",
'september':"its september",
'october':"its october",
'november':"its november",
'december':None
}
def index(request):
   month=list(dict.keys())
   #capitalize=month.capitalize()
   return render(request,"index.html", {'months':month})
def number(request,month):
	if month<len(dict):
		no=list(dict.keys())
		m=no[month-1]
		return HttpResponseRedirect(m)
	else:
		raise Http404()
def months(request, month):
	try:
		text=dict[month]
		if text is not None:
			return render(request,'index.html',{'test':text,'month':month})
		else:
			return HttpResponse("<h2>There is no task assigned</h2>")
		
	except:
		raise Http404("Hello World")
