from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('order/',views.order,name='order'),




]