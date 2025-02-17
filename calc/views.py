from django.shortcuts import render,redirect
from calc.models import foods , userinfo

def home(request):
    return render(request, 'home1.html')

def signup(request):
    if request.method == "POST":
       username = request.POST.get('name')
       password = request.POST.get('password')
       cpassword = request.POST.get('retypepassword')
       email = request.POST.get('email')
       number = request.POST.get('number')
       address = request.POST.get('address')
       pin = request.POST.get('pin')
       user = userinfo.objects.create(name=username,email=email,number=number,password=password,pin=pin,address=address)
       user.save();
       return redirect('mainpage')
    return render(request, 'signup.html')
def login(request):
    if request.method=="POST":
        username = request.POST['name']
        password = request.POST['password']
        user = userinfo.objects.filter(name=username,password=password)
        if user:
            return redirect('mainpage')
        else:
            return render(request,'login.html',{'massage':'invalid'})
    else:
        return render(request,'login.html')

def mainpage(request):
    food = foods.objects.all()
    return render(request, 'main.html', {'fooditems':food})
