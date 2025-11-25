from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def produce(request):
    return HttpResponse("PRRODUCE IS THE FEED OF THE FARMER.")