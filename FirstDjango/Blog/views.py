from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Function(request):
	#print("Hello Djngo Girls Bhavnagar")
	return HttpResponse("<h1>Hello</h1>")
