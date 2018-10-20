from django.shortcuts import render, redirect

def orders_index(request):
    return render(request, 'orders/orders_index.html')
