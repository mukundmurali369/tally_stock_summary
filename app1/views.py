from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *


# Create your views here.
def base(request):
    return render(request, 'base.html')

def load_stock_summarys(request):
    return render(request, 'load_stock_summarys.html')

def load_stock_group(request):
    return render(request, 'load_stock_group.html')

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
        grp=Stock_Group(
            Group_name=Group_namee
        )
        grp.save()
        print("hii")
        return redirect('/')


def input_group_items(request):
    grp=Stock_Group.objects.all()
    return render(request, 'input_group_items.html',{'grp':grp})

def save_group_items(request):
    if request.method=='POST':
        
        Groupp=request.POST['Group']
        Item_namee=request.POST['Item_name']
        Quantityy=request.POST['Quantity']
        Ratee =request.POST['Rate ']
        Valuee=request.POST['Value']
        grp=Stock_Group_items(
            Group=Groupp,
            Item_name=Item_namee,
            Quantity=Quantityy,
            Rate=Ratee,
            Value=Valuee,
        )
        grp.save()
        print("hii")
        return redirect('/')