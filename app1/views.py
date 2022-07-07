from django.shortcuts import render
from .models import *


# Create your views here.
def base(request):
    return render(request, 'base.html')
    
def load_stock_summarys(request):
    return render(request, 'load_stock_summarys.html')

def load_stock_group(request):
    return render(request, 'load_stock_group.html')

