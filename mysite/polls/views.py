from django.shortcuts import render

from django.http import HttpResponse

#first view
def index(request):
    return HttpResponse("Awesome, at the polls index.")
