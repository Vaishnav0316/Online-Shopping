from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.http import JsonResponse
from seller.models import *
import datetime
def buyerReg(request):
    return render(request,'buyerReg.html')
def buyerRegAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['DOB']
    country=request.POST['country']
    Phonenumber=request.POST['phonenumber']
    username=request.POST['username']
    password=request.POST['password']
    user=buyer_tb(Name=name,Gender=gender,DOB=dob,Country=country,PhoneNumber=Phonenumber,Username=username,Password=password)
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
def ProfileUpdate(request):
    id=request.session["buyer_id"]
    user=buyer_tb.objects.filter(id=id)
    return render(request,'ProfileUpdate.html',{'upd':user})
def updateAction(request):
    id=request.POST['id']
    name=request.POST['name']
    gender=request.POST['gender']
    DOB=request.POST['DOB']
    country=request.POST['country']
    phonenumber=request.POST['phonenumber']
    username=request.POST['username']
    edit=buyer_tb.objects.filter(id=id).update(Name=name,Gender=gender,DOB=DOB,Country=country,PhoneNumber=phonenumber,Username=username)
    messages.add_message(request,messages.INFO,"Profile Updated")
    return render(request,"buyerhome.html")
def viewproduct_buy(request):
    user=product_tb.objects.all()
    return render(request,'viewproduct_buy.html',{'vp':user})
def addtocart(request,id):
    user=product_tb.objects.filter(id=id)
    return render(request,'addtocart.html',{'ac':user})
def addtocartAction(request):
    pid=request.POST['id']
    bid=request.session["buyer_id"]
    quantity=request.POST['quantity']
    total=request.POST['total']
    stock=request.POST['stock']
    if(int(quantity)>int(stock)):
        messages.add_message(request,messages.INFO,"Quantity exceeded")
        return render(request,"buyerhome.html")
    else:
        cart=cart_tb(Quantity=quantity,Total=total,Productid_id=pid,Buyerid_id=bid)
        cart.save()
        messages.add_message(request,messages.INFO,"Added to Cart")
        return render(request,"buyerhome.html")
def Viewcart(request):
    grandtotal=0
    b_id=request.session["buyer_id"]
    cart=cart_tb.objects.filter(Buyerid=b_id)
    if(len(cart)!=0):
        for i in cart:
            total=i.Total
            grandtotal+=total
        return render(request,'Viewcart.html',{'ca':cart,'gt':grandtotal})
    else:
        messages.add_message(request,messages.INFO,"Cart is empty")
        return render(request,"buyerhome.html")

def delete_cart(request,id):
    user=cart_tb.objects.filter(id=id).delete()
    return redirect("Viewcart")
def orderAction(request):
    bid=request.session["buyer_id"]
    user=cart_tb.objects.filter(Buyerid=bid)
    C_name=request.POST['name']
    Address=request.POST["Shipingaddress"]
    Phone=request.POST['number']
    grtotal=request.POST['gtotal']
    orderdate=datetime.date.today()
    ordertime=datetime.datetime.now().strftime("%H:%M")
    order=order_tb(customer_name=C_name,Address=Address,Phonenumber=Phone,GrandTotal=grtotal,Buyerid_id=bid,OrderDate=orderdate,OrderTime=ordertime)
    order.save()
    for i in user:
        item=cart_tb.objects.filter(id=i.id)
        Orderid=order.id
        pid=item[0].Productid.id
        Quantity=item[0].Quantity
        newstock=item[0].Productid.Stock-Quantity
        Total=item[0].Total
        new_stock=product_tb.objects.filter(id=pid).update(Stock=newstock)
        orderitem=orderitems_tb(Orderid_id=Orderid,Productid_id=pid,Buyerid_id=bid,Quantity=Quantity,Total=Total)
        
        orderitem.save()
    return redirect('payment',order.id)
def searchAction(request):
    search=request.POST['search']
    searchitem=product_tb.objects.filter(Name__istartswith=search)
    return render(request,'viewproduct_buy.html',{'vp':searchitem})  
def payment(request,id):
    pay=order_tb.objects.filter(id=id)
    return render(request,'payment.html',{'pa':pay})
def payAction(request):
    order=request.POST['oid']
    bid=request.session["buyer_id"]
    name=request.POST['name']
    cnumber=request.POST['cnum']
    cvv=request.POST['cvv']
    expdate=request.POST['expiry']
    pay=pay_tb(Name=name,CardNumber=cnumber,CVV=cvv,Exp_Date=expdate,Buyerid_id=bid,Orderid_id=order)
    pay.save()
    cart_tb.objects.filter(Buyerid_id=bid).delete()
    messages.add_message(request,messages.INFO,"Payment Successfull")
    return render(request,"buyerhome.html")
def Vieworder(request):
    bid=request.session["buyer_id"]
    order=order_tb.objects.filter(Buyerid_id=bid)
    return render(request,"Vieworder.html",{'or':order})
def details(request,id):
    details=order_tb.objects.filter(id=id)
    items=orderitems_tb.objects.filter(Orderid_id=id)
    return render(request,"Vieworder_detail.html",{'det':details,'it':items})
def CancelOrder(request,id):
    cancel=order_tb.objects.filter(id=id).update(Status="Cancelled")
    messages.add_message(request,messages.INFO,"Order has been cancelled")
    return render(request,"buyerhome.html")
def TrackingDetails(request,id):
    track=Tracking_tb.objects.filter(Orderid_id=id)
    if(len(track) > 0):
        return render(request,"trackingdet.html",{'tr':track})
    else:
        messages.add_message(request,messages.INFO,"No tracking Details yet")
        return render(request,"buyerhome.html")
def ResetPassword(request):
    return render(request,"ResetPassword.html")
def resetAction(request):
    bid=request.session["buyer_id"]
    user=buyer_tb.objects.filter(id=bid)
    oldpswd=request.POST['oldpswd']
    newpswd=request.POST['newpswd']
    confpswd=request.POST['confirmpswd']
    if(user[0].Password == oldpswd):
        if(newpswd == confpswd):
            newpass=buyer_tb.objects.filter(id=bid).update(Password=newpswd)
            messages.add_message(request,messages.INFO,"Reset successfull")
        else:
            messages.add_message(request,messages.INFO,"Password does not match")  
    else:
        messages.add_message(request,messages.INFO,"Password is incorrect") 
        
    return render(request,"buyerhome.html")










 



