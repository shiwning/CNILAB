import django
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from license.dbsearch import searchAll


def status(request):
    context = {}
    context['license_table'] = searchAll('license')
    context['client_table'] = searchAll('client')
    return render(request, 'status.html', context)
