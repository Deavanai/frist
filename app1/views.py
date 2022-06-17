from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def babu(request):
    return HttpResponse('y says hello ALL')