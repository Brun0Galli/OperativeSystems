from django.shortcuts import render
from django.http import HttpResponse and JsonResponse
from .PlanificationAlgorithms import execute_planification_algorithm
# Create your views here.

def IndexView(request):
    return HttpResponse('Hello World')

# Path: ProtecyoSO\APP1\urls.py
def Hla(request):
    return HttpResponse('Hola Mundo')

def bubble_sort(request):
    return render(request, 'sorting.html')

def run_planification_algorithm(request):
    processes = request.GET.get('processes')
    quantum = request.GET.get('quantum')
    algorithm = request.GET.get('algorithm')
    processes = eval(processes)
    quantum = int(quantum)
    completion_time, process_names = execute_planification_algorithm(algorithm, processes, quantum)
    return JsonResponse({'completion_time': completion_time, 'process_names': process_names})