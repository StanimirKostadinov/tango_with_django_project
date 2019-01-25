from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    message = ''' Rango says hey tehre partner!
	<br/> %s <a href='/rango/about/'>About</a>
	'''
    return HttpResponse(message )

def about(request):
    message = '''
	Rango says here is the about page.	
	<h2><a href='/rango/'>Index</a><h2> '''
    return HttpResponse(message )
