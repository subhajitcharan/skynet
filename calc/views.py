from django.shortcuts import render,redirect
from calc.models import foods ,extrauserinfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    if request.method=="POST":
        if not request.user.is_authenticated:
            return
        order={}
        for key, value in request.POST.items():
            if key.startswith("quantity_") and value.isdigit() and int(value) > 0:
                food_id = key.split("_")[1]
                quantity = int(value)
                        
                food_item = foods.objects.get(id=food_id)
                
                order[food_item.name]=quantity
                
                
                
        return render(request,'invoice.html',{'orders':order,'username':request.user.username})
        
    else:
        food = foods.objects.all()
        return render(request,"home1.html", {'fooditems':food})

    

def signup_page(request):
    if request.method == "POST":
       username = request.POST.get('name')
       password = request.POST.get('password')
       email = request.POST.get('email')
       number = request.POST.get('number')
       address = request.POST.get('address')
       pin = request.POST.get('pin')
       if User.objects.filter(email=email,username=username):
            print("mail or username already exists")
            return render(request,'signup.html',{'massage':'mail already exists'})
       else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save();
            Extrauserinfo= extrauserinfo.objects.create(email=email,name=username,number=number,pin=pin,address=address)
            Extrauserinfo.save();
            login(request,user)
            return redirect('/')
    else:
        return render(request, 'signup.html')
def login_page(request):
    if request.method=="POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'message':'invalid'})
    else:
        return render(request,'login.html')

        
def userlogout(request):
    logout(request)
    return redirect('/')
