from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . import dbsearch

def deleteLicense(request):
    if request.method == "GET":
        if dbsearch.deleteLicense(request.GET.get('Lno'))==True:
            return redirect('/')
        else:
            return redirect('/')
    return redirect('/')

def deleteClient(request):
    if request.method == "GET":
        if dbsearch.deleteClient(request.GET.get('Tno'),request.GET.get('Lno'))==True:
            return redirect('/')
        else:
            return redirect('/')
    return redirect('/')