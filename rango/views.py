from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    message = "Rango says hey tehre partner!"
	
	html ="<br/> <a href='/rango/about/'>About</a>"
	
     return HttpResponse("%s" + "/n" + " %s " % (message, html))

def about(request):
    message =  "Rango says here is the about page."	
	html = "<a href='/rango/'>Index</a>"
    return HttpResponse("%s" + "/n" + " %s " % (message, html))
