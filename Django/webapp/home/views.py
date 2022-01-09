from django.shortcuts import render, HttpResponse
from home.models import contact
from datetime import datetime


# Create your views here.
def index(request):
	#return HttpResponse("This is our home page")
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def contact(request):
	if request.method == "POST":
		name1=request.POST.get('name')
		email1=request.POST.get("email")
		phone1=request.POST.get("phone")
		desc1=request.POST.get("desc")
		Contact=contact(nm = name1, email = email1, phone = phone1, desc = desc1, date = datetime.today() )
		Contact.save()
	    
	return render(request,'contact.html')
