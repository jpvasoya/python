from django.shortcuts import render
from django.http import HttpResponse,Http404
from datetime import date
all_posts=[
{
'slug':'python-blog',
'post_title':'python',
'post_img':'python.png',
'date':date(2020,10,15),
'post_details':"""
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.""",
'post_excerpt':"""Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.""",
'post_author':'Jp Vasoya'
},
{
'slug':'php-blog',
'post_title':'php',
'post_img':'php.jpg',
'date':date(2021,10,15),
'post_details':"""
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.""",
'post_excerpt':"""Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.""",
'post_author':'Jp Vasoya'
},
{
'slug':'javascript-blog',
'post_title':'Javascript',
'post_img':'javascript.png',
'date':date(2017,10,15),
'post_details':"""
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.""",
'post_excerpt':"""Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.""",
'post_author':'Jp Vasoya'
},
{
'slug':'c-langauge-blog',
'post_title':'C Programming',
'post_img':'c-programming.png',
'date':date(2022,10,15),
'post_details':"""
A successor to the programming language B, C was originally developed at Bell Labs by Dennis Ritchie between 1972 and 1973 to construct utilities running on Unix. It was applied to re-implementing the kernel of the Unix operating system.[6] During the 1980s, C gradually gained popularity. It has become one of the most widely used programming languages,[7][8] with C compilers from various vendors available for the majority of existing computer architectures and operating systems. C has been standardized by ANSI since 1989 (ANSI C) and by the International Organization for Standardization (ISO).""",
'post_excerpt':"""C is a powerful general-purpose programming language. It can be used to develop software like operating systems, databases, compilers, and so on.""",
'post_author':'Jp Vasoya'
},
]

def get_date(post):
	return post['date']
# Create your views here.
def index(request):
	sorted_posts=sorted(all_posts, key=get_date)
	latest_posts=sorted_posts[-2:]
	return render(request, "blog/index.html",
	{'posts':latest_posts})	
#	return HttpResponse("its Work")
def posts(request):
	sorted_posts=sorted(all_posts, key=get_date)
	latest_posts=sorted_posts[:]
	return render(request, "blog/all_posts.html",
	{'posts':latest_posts})
	#return render(request,"blog/all_posts.html")
def post_details(request,slug):
	try:
		posts=next(post for post in all_posts if post['slug']==slug)
		return render(request, "blog/post_detail.html",{ 'post':posts})
	except:
		raise Http404()
	