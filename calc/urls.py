from django.urls import path
from calc import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup',views.signup,name='signup'),
    path('mainpage',views.mainpage,name='mainpage'),
    path('login',views.login,name='login'),
]