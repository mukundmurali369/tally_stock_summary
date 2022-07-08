from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.base,name='base'),
    path('load_stock_summarys',views.load_stock_summarys,name='load_stock_summarys'),
    path('load_stock_group',views.load_stock_group,name='load_stock_group'),
    path('load_item_details',views.load_item_details,name='load_item_details'),
    path('load_stock_voucher',views.load_stock_voucher,name='load_stock_voucher'),

]