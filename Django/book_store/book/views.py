from django.shortcuts import render
from .models import Books
from django.http import Http404

def index(request):
	books=Books.objects.all()
	return render(request,"index.html",
	{
	"books":books
	})
def books(request,slug):
	try:
		book=Books.objects.get(slug=slug)
	except:
		raise Http404()
	return render(request,"books.html",
	{
	"title":book.title,
	"author":book.author,
	"bestSeller":book.bestSeller,
	"rating":book.rating,
	"desc":book.desc
	})