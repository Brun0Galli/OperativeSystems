import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

st.title('Visualización del algoritmo de ordenamiento de burbuja')

arr = st.text_input('Ingrese una lista de números separados por comas (ejemplo: 5, 2, 7, 1)', '5, 2, 7, 1')
arr = [int(x.strip()) for x in arr.split(',')]

if st.button('Ordenar'):
    st.write('Lista original:', arr)
    bubble_sort(arr)
    st.write('Lista ordenada:', arr)


