from django.http import HttpResponse
from datetime import date
def index(request):
	time=date()
	return HttpResponse(time)