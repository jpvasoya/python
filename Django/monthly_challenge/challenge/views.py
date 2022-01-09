from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
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
'december':'its december'
}
def index(request):
    list_items=""
    months=list(dict.keys())
    
    for month in months:
    	capitalized_month=month.capitalize()
    	month_path=reverse('index',args=[month])
    	list_items+=f"""<li><a <a href='{month_path}'>{capitalized_month}</a></li>"""
    	response_data=f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
def number(request,month):
	no=list(dict.keys())
	m=no[month-1]
	return HttpResponseRedirect(m)
def months(request, month):
	try:
		if month in dict:
		   text=dict[month]
		return HttpResponse("<h1><a href='/'>Back</a></h1>"+text)
	except:
			return HttpResponseNotFound("Its Not valid")