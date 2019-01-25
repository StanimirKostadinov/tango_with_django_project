from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    message = "Rango says hey tehre partner!"
	
	html =" <a href='/rango/about/'>About</a>"
	
    return HttpResponse("%s  %s " % (message, html) )

def about(request):
    message =  "Rango says here is the about page."	
	html = "<h2><a href='/rango/'>Index</a><h2> '''
    return HttpResponse("%s  %s " % (message, html))
