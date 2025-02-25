from django.urls import path
from calc import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup_page',views.signup_page,name='signup'),
    
    path('login_page',views.login_page,name='login'),
    path('userlogout',views.userlogout,name='logout'),
]