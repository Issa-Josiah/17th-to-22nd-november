from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def monday(request):
    return HttpResponse('Welcome to Thursday a wonderful day')
def boot(request):
    return render(request, 'boot/index.html')