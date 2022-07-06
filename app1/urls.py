from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.base,name='base'),
    path('load_stock_summary',views.load_stock_summary,name='load_stock_summary'),

]