from django.http import HttpRequest
from django.shortcuts import render
from app.models import *
from django.db.models import Sum,F


def index(request):
   
    return render(request,
                  'app/home/index.html')