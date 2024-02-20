from django.shortcuts import render,redirect
from Site_admin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=admin_tb.objects.filter(Username=username,Password=password)
    buyerUser=buyer_tb.objects.filter(Username=username,Password=password)
    sellerUser=seller_tb.objects.filter(Username=username,Password=password)
    if(user.count()>0):
        request.session["id"]=user[0].id
        return render(request,'adminhome.html')
        messages.add_message(request,messages.INFO,"Login Succesfull")
    elif(buyerUser.count()>0):
        request.session["buyer_id"]=buyerUser[0].id
        messages.add_message(request,messages.INFO,"Login Succesfull")
        return render(request,'buyerhome.html')
    elif(sellerUser.count()>0):
        if(sellerUser[0].Status=="Approved"):
            request.session["seller_id"]=sellerUser[0].id
            messages.add_message(request,messages.INFO,"Login Succesfull")
            return render(request,'sellerhome.html')
        else:
            messages.add_message(request,messages.INFO,"Your request has not been approved")
            return redirect("login")
    else:
        messages.add_message(request,messages.INFO,"Invalid username or password")
        return render(request,"login.html")
def add_category(request):
    return render(request,"add_category.html")
def SaveAction(request):
    category=request.POST['category']
    user=category_tb(Category_Name=category)
    user.save()
    messages.add_message(request,messages.INFO,"Saved Succesfully")
    return redirect("index")
def view_seller(request):
    user=seller_tb.objects.all()
    return render(request,'view_seller.html',{'se':user})
def approve(request,id):
    user=seller_tb.objects.filter(id=id).update(Status="Approved")
    return redirect("view_seller")
def reject(request,id):
    user=seller_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect("view_seller")
def forgotpswd(request):
    return render(request,"forgotpswd.html")
def nextAction(request):
    username=request.POST['uname']
    seller=seller_tb.objects.filter(Username=username)
    buyer=buyer_tb.objects.filter(Username=username)
    if(buyer.count()>0):
        return render(request,"newpswd.html",{'us':username})
    elif(seller.count()>0):
        return render(request,"newpswd.html",{'us':username})
    else:
        messages.add_message(request,messages.INFO,"Invalid username")
        return redirect("login")
    
def nextAction2(request):
    username=request.POST['uname']
    name=request.POST['name']
    dob=request.POST['DOB']
    phnum=request.POST['phonenumber']
    buyer=buyer_tb.objects.filter(Name=name,DOB=dob,PhoneNumber=phnum)
    seller=seller_tb.objects.filter(Name=name,DOB=dob,PhoneNumber=phnum)
    if(buyer.count()>0):
        return render(request,"changepswd.html",{'us':username})
    elif(seller.count()>0):
        return render(request,"changepswd.html",{'us':username})
    else:
        messages.add_message(request,messages.INFO,"Data is incorrect")
        return redirect("login")
def resetAction_admin(request):
    username=request.POST['uname']
    seller=seller_tb.objects.filter(Username=username)
    buyer=buyer_tb.objects.filter(Username=username)
    newpswd=request.POST['newpswd']
    confpswd=request.POST['confirmpswd']
    if(newpswd==confpswd):
        if(seller.count()>0):
            seller=seller_tb.objects.filter(Username=username).update(Password=newpswd)
            messages.add_message(request,messages.INFO,"Reset successfull")
        elif(buyer.count()>0):
            buyer=buyer_tb.objects.filter(Username=username).update(Password=newpswd)
            messages.add_message(request,messages.INFO,"Reset successfull")
    else:
        messages.add_message(request,messages.INFO,"Password is incorrect")
    return redirect("login")
        
    
    




    

    

