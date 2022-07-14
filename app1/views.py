from calendar import month
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
    items=Buy_or_sell_items.objects.filter(Group_id=pk)
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
    print(b)


    context={'items':items,'money':a,'qnty':b}

    return render(request, 'load_stock_group.html',context)

def load_item_details(request,pk):
    items=Buy_or_sell_items.objects.filter(Item_name_id = pk)
    print(pk)
    print(items)
    

    July=Buy_or_sell_items.objects.filter(month ="July",BorS="1")
    m_jly=July.values_list('Value',flat=True)
    print(m_jly)
    a =0
    for i in m_jly:
        a=a+i
    print(a)
    qnty=July.values_list('Quantity',flat=True)
    print(qnty)
    b =0
    for i in qnty:
        b=b+i
    print(a)

    Open=Buy_or_sell_items.objects.filter(BorS="3")
    print(Open)
    
    m_open_val=Open.values_list('Value',flat=True)
    print(m_open_val)
    c =0
    for i in m_open_val:
        c=c+i
    print(c)

    m_open_qun=Open.values_list('Quantity',flat=True)
    print(m_open_qun)
    d =0
    for i in m_open_qun:
        d=d+i
    print(d)
    
    context={'Julyv':a,'Julyq':b,'openv':c,'openq':d,}
    return render(request, 'load_item_details.html',context)

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
        Item_unitt=request.POST['Item_unit']
        
        Group_obj=Stock_Groups.objects.get(id=Groupp)

        grp=Add_items(
            Group=Group_obj,
            Item_name=Item_namee,
            Item_unit=Item_unitt,
            
        )
        grp.save()
        return redirect('/')



def input_buy_items(request):
    grp=Stock_Groups.objects.all()
    itm=Add_items.objects.all()
    context={'grp':grp,'items':itm}
    return render(request, 'input_buy_items.html',context)
        
def save_buy_item(request):
    if request.method=='POST':
        
        Groupp=request.POST['Group']
        Item_namee=request.POST['Item_name']
        Quantityy=request.POST['Quantity']
        companyy  =request.POST['company']
        Ratee =request.POST['Rate']
        datee =request.POST['date']
        monthh =request.POST['month']
        Valuee=int(Ratee)*int(Quantityy)
        Group_obj=Stock_Groups.objects.get(id=Groupp)
        Items_obj= Add_items.objects.get(id=Item_namee)

        buy=Buy_items(
            Group=Group_obj,
            Item_name=Items_obj,
            Quantity=Quantityy,
            Rate=Ratee,
            Value=Valuee,
            company=companyy,
            date=datee,
            month=monthh,

        )
        buy.save()
        return redirect('/')




def buy_or_sell_items(request):
    grp=Stock_Groups.objects.all()
    itm=Add_items.objects.all()
    context={'grp':grp,'items':itm}
    return render(request, 'buy_or_sell_items.html',context)


def save_buy_or_sell_item(request):
    if request.method=='POST':
        
        Groupp=request.POST['Group']
        Item_namee=request.POST['Item_name']
        BorSS=request.POST['BorS']
        Quantityy=request.POST['Quantity']
        companyy  =request.POST['company']
        Ratee =request.POST['Rate']
        datee =request.POST['date']
        monthh =request.POST['month']
        Valuee=int(Ratee)*int(Quantityy)
        Group_obj=Stock_Groups.objects.get(id=Groupp)
        Items_obj=Add_items.objects.get(id=Item_namee)

        buyorsell=Buy_or_sell_items(
            Group=Group_obj,
            Item_name=Items_obj,
            BorS=BorSS,
            Quantity=Quantityy,
            Rate=Ratee,
            Value=Valuee,
            company=companyy,
            date=datee,
            month=monthh,

        )
        buyorsell   .save()
        return redirect('/')