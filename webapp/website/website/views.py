from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

def index(request):
    response = request
    context = dict()
    return render(response,'index.html',context)
