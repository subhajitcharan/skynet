from django.urls import path
from . import views
urlpatterns = [
    path('ownerlogin', views.ownerlogin, name='ownerlogin'),
    path('orderinfo', views.orderinfo, name='orderinfo'),
   
]