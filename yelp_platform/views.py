from django.shortcuts import render

# Create your views here.
def index(request):
	""" landing page """
	# make it look good, bootstrap fun!! 
	return HttpResponse("All Ok")