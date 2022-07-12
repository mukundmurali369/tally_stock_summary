from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.base,name='base'),
    path('load_stock_summarys',views.load_stock_summarys,name='load_stock_summarys'),
    path('load_stock_group',views.load_stock_group,name='load_stock_group'),
    path('load_item_details',views.load_item_details,name='load_item_details'),
    path('load_stock_vouchers',views.load_stock_vouchers,name='load_stock_vouchers'),
    path('load_voucher_receipt',views.load_voucher_receipt,name='load_voucher_receipt'),
    path('input_group',views.input_group,name='input_group'),
    path('save_group',views.save_group,name='save_group'),
    path('input_group_items',views.input_group_items,name='input_group_items'),
    path('save_group_items',views.save_group_items,name='save_group_items'),



]