from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    context = {'hi': 'INDEX'}
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(context, request))
