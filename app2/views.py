from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mugi(request):
    return HttpResponse('m says hello ALL')


