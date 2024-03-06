from django.urls import path
from . import views

urlpatterns = [
    path('hla/', views.Hla, name='hla'),
    path('', views.bubble_sort, name='bubble_sort'),
    path('run_planification_algorithm/', views.run_planification_algorithm, name='run_planification_algorithm'),
]