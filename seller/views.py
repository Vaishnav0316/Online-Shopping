from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.http import JsonResponse
from Site_admin.models import *
from buyer.models import *
import datetime
def sellerReg(request):
    return render(request,'sellerReg.html')
def sellerRegAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['DOB']
    country=request.POST['country']
    Phonenumber=request.POST['phonenumber']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image="no pic"
    username=request.POST['username']
    password=request.POST['password']
    user=seller_tb(Name=name,Gender=gender,DOB=dob,Country=country,PhoneNumber=Phonenumber,File=image,Username=username,Password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration was suucessfull")
    return render(request,"index.html")
def checkuser(request):
    user=request.GET['us']
    username=buyer_tb.objects.filter(Username=user)
    if(username.count()>0):
        msg='exist'
    else:
        msg='notexist'
    return JsonResponse({'valid':msg})
def Sellerprofileupdate(request):
    id=request.session["seller_id"]
    user=seller_tb.objects.filter(id=id)
    return render(request,'Sellerprofileupdate.html',{'upd':user})
def sellerupdateAction(request):
    id=request.POST['id']
    user=seller_tb.objects.filter(id=id)
    name=request.POST['name']
    gender=request.POST['gender']
    DOB=request.POST['DOB']
    country=request.POST['country']
    phonenumber=request.POST['phonenumber']
    if(len(request.FILES)>0):
        file=request.FILES['image']
    else:
        file=user[0].File
    username=request.POST['username']
    edit=seller_tb.objects.filter(id=id).update(Name=name,Gender=gender,DOB=DOB,Country=country,PhoneNumber=phonenumber,Username=username)
    img=seller_tb.objects.get(id=id)
    img.File=file
    img.save()
    messages.add_message(request,messages.INFO,"Profile Updated")
    return render(request,"sellerhome.html")
def Add_Product(request):
    category=category_tb.objects.all()
    return render(request,'Add_Product.html',{'ca':category})
def saveAction(request):
    name=request.POST['name']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image="no pic"
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    category=request.POST['category']
    sellerid=request.session["seller_id"]
    user=product_tb(Name=name,File=image,Price=price,Stock=stock,Details=details,Categoryid_id=category,Sellerid_id=sellerid)
    user.save()
    messages.add_message(request,messages.INFO,"Saved sucessfully")
    return render(request,"sellerhome.html") 
def ViewProduct(request):
    id=request.session["seller_id"]
    user=product_tb.objects.filter(Sellerid_id=id)
    return render(request,'ViewProduct.html',{'vp':user})
def edit(request,id):
    user=product_tb.objects.filter(id=id)
    cat=category_tb.objects.all()
    return render(request,'edit.html',{'ed':user,'ca':cat})
def editAction(request):
    id=request.POST['id']
    user=product_tb.objects.filter(id=id)
    name=request.POST['name']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image=user[0].File
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    category=request.POST['category']
    user=product_tb.objects.filter(id=id).update(Name=name,Price=price,Stock=stock,Details=details,Categoryid_id=category)
    img=product_tb.objects.get(id=id)
    img.File=image
    img.save()
    messages.add_message(request,messages.INFO,"Saved sucessfully")
    return render(request,"sellerhome.html")   
def delete(request,id):
    product_tb.objects.filter(id=id).delete()
    return redirect("ViewProduct")
def ViewOrder_seller(request):
    sid=request.session['seller_id']
    product=product_tb.objects.filter(Sellerid_id=sid)
    item=orderitems_tb.objects.filter(Productid_id__in=product)
    #order=order_tb.objects.filter(id__in=item)
    for ord in item:
        orderid=ord.Orderid_id
        order=order_tb.objects.filter(id=orderid)
    return render(request,"ViewOrder_seller.html",{'ors':item})
def details_seller(request,id):
    sid=request.session['seller_id']  
    prdct=product_tb.objects.filter(Sellerid_id=sid) 
    items=orderitems_tb.objects.filter(Orderid_id=id,Productid_id__in=prdct)
    details=order_tb.objects.filter(id=id)
    return render(request,"details_seller.html",{'de':details,'it':items})
def Approve_prdct(request,id):
    user=order_tb.objects.filter(id=id).update(Status="Approved")
    return redirect("ViewOrder_seller")
def Reject_prdct(request,id):
    user=order_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect("ViewOrder_seller")
def Confirmreject(request,id):
    oid=orderitems_tb.objects.filter(Orderid_id=id)
    for i in oid:
        pid=i.Productid_id
        prdct=product_tb.objects.filter(id=pid)
        stock=prdct[0].Stock
        quantity=i.Quantity
        newstock=stock+quantity
        new_stock=product_tb.objects.filter(id=pid).update(Stock=newstock)
    order=order_tb.objects.filter(id=id).update(Status="Cancelled")
    return render(request,"sellerhome.html")
def Track(request,id):
    order=order_tb.objects.filter(id=id)
    return render(request,"Track.html",{'id':order})
def SendAction(request):
    oid=request.POST['id']
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    send=Tracking_tb(Orderid_id=oid,Details=details,Time=time,Date=date)
    send.save()
    messages.add_message(request,messages.INFO,"Sucessfull")
    return render(request,"sellerhome.html")
def ResetPassword_seller(request):
    return render(request,"ResetPassword_seller.html")
def resetAction_seller(request):
    sid=request.session["seller_id"]
    user=seller_tb.objects.filter(id=sid)
    oldpswd=request.POST['oldpswd']
    newpswd=request.POST['newpswd']
    confpswd=request.POST['confirmpswd']
    if(user[0].Password == oldpswd):
        if(newpswd == confpswd):
            newpass=seller_tb.objects.filter(id=sid).update(Password=newpswd)
            messages.add_message(request,messages.INFO,"Reset successfull")
        else:
            messages.add_message(request,messages.INFO,"Password does not match")  
    else:
        messages.add_message(request,messages.INFO,"Password is incorrect") 
        
    return render(request,"sellerhome.html")
def logout(request):
    request.session.flush()
    return redirect('login')


    


    

    




