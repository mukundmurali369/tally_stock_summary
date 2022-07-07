from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.base,name='base'),
    path('load_stock_summarys',views.load_stock_summarys,name='load_stock_summarys'),
    path('load_stock_group',views.load_stock_group,name='load_stock_group'),

]