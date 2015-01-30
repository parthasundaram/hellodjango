from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
	""" landing page """
	# make it look good, bootstrap fun!! 
	return HttpResponse("All Ok")