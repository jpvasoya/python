from django.http import HttpResponse
from django.shortcuts import render
def try1(request):
	return render(request, 't1.html')

def removepunc(request):
     return render(request, 't2.html',rp)