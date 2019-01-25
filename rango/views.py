from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    message = "Rango says hey tehre partner!"
    return HttpResponse(" <br/> %s <a href='/rango_/about/'>About</a>"  % message )

def about(request):
    message = 'Rango says here is the about page.'
    return HttpResponse(" %s <a href='/rango_/'>Index</a>" % message)
