from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def IndexView(request):
    return HttpResponse('Hello World')

# Path: ProtecyoSO\APP1\urls.py
def Hla(request):
    return HttpResponse('Hola Mundo')

def bubble_sort(request):
    return render(request, 'sorting.html')