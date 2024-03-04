from django.urls import path
from . import views

urlpatterns = [
    path('hla/', views.Hla, name='hla'),
    path('', views.bubble_sort, name='bubble_sort'),

]