from django.shortcuts import render,redirect
from calc.models import foods,ownerinfo

def orderinfo(request):
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('foodimage')
        food = foods.objects.create(name=name,price=price,description=description,image=image)
        food.save();
        return redirect('orderinfo')
    return render(request, 'orderinfo.html')

def ownerlogin(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        owner=ownerinfo.objects.filter(name=name,password=password)
        if owner:
           return redirect('orderinfo')
        else:
            return render(request,'ownerlogin.html')
        
    return render(request,'ownerlogin.html')
    

