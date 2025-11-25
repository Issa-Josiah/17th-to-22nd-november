from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def produce(request):
    context = {'producer': 'Welcome Home'}
    return render(request, '../../html/thursday.html', context)