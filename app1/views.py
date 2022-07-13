from multiprocessing import context
from re import I
from django.contrib import messages
from sys import flags
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *


# Create your views here.
def base(request):
    return render(request, 'base.html')

def load_stock_summarys(request):
    stk=Stock_Groups.objects.all()
    money=stk.values_list('Group_total',flat=True)
    print(money)
    a =0
    for i in money:
        a=a+i
    print(a)

    context={'stk':stk,'money':a}
    
    return render(request, 'load_stock_summarys.html',context)

def load_stock_group(request,pk):
    items=Stock_Group_items.objects.filter(Group_id=pk)
    money=items.values_list('Value',flat=True)
    print(money)
    a =0
    for i in money:
        a=a+i
    print(a)

    qnty=items.values_list('Quantity',flat=True)
    print(qnty)
    b =0
    for i in qnty:
        b=b+i
    print(a)


    context={'items':items,'money':a,'qnty':b}

    return render(request, 'load_stock_group.html',context)

def load_item_details(request):
    return render(request, 'load_item_details.html')

def load_stock_vouchers(request):
    return render(request, 'load_stock_vouchers.html')

def load_voucher_receipt(request):
    return render(request, 'load_voucher_receipt.html')

def input_group(request):
    return render(request, 'input_group.html')

def save_group(request):
    if request.method=='POST':
        
        Group_namee=request.POST['Group_name']
        grp=Stock_Groups(
            Group_name=Group_namee
        )
        grp.save()
        print("hii")
        return redirect('/')


def input_group_items(request):
    grp=Stock_Groups.objects.all()
    return render(request, 'input_group_items.html',{'grp':grp})

def save_group_item(request):
    if request.method=='POST':
        
        Groupp=request.POST['Group']
        Item_namee=request.POST['Item_name']
        Quantityy=request.POST['Quantity']
        Ratee =request.POST['Rate']
        Valuee=int(Ratee)*int(Quantityy)
        Group_obj=Stock_Groups.objects.get(id=Groupp)

        grp=Stock_Group_items(
            Group=Group_obj,
            Item_name=Item_namee,
            Quantity=Quantityy,
            Rate=Ratee,
            Value=Valuee,
        )
        grp.save()
        Items=Stock_Group_items.objects.filter(Group_id =Group_obj).values_list('Value',flat=True)
        print(Items)
        a =0
        for i in Items:
            a=a+i
        print(a)
       
        Group_obj.Group_total = a
        Group_obj.save()
        print("hii")
        return redirect('/')