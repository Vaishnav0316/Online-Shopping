"""
URL configuration for online_Shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Site_admin import views as adminview
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('add_category/',adminview.add_category,name="add_category"),
    path('SaveAction/',adminview.SaveAction,name="SaveAction"),
    path('buyerReg/',buyerview.buyerReg,name="buyerReg"),
    path('buyerRegAction/',buyerview.buyerRegAction,name="buyerRegAction"),
    path('checkuser/',buyerview.checkuser,name="checkuser"),
    path('ProfileUpdate/',buyerview.ProfileUpdate,name="ProfileUpdate"),
    path('updateAction/',buyerview.updateAction,name="updateAction"),
    path('sellerReg/',sellerview.sellerReg,name="sellerReg"),
    path('sellerRegAction/',sellerview.sellerRegAction,name="sellerRegAction"),
    path('Sellerprofileupdate/',sellerview.Sellerprofileupdate,name="Sellerprofileupdate"),
    path('sellerupdateAction/',sellerview.sellerupdateAction,name="sellerupdateAction"),
    path('view_seller/',adminview.view_seller,name="view_seller"),
    path('approve<int:id>/',adminview.approve,name="approve"),
    path('reject<int:id>/',adminview.reject,name="reject"),
    path('Add_Product/',sellerview.Add_Product,name="Add_Product"),
    path('saveAction/',sellerview.saveAction,name="saveAction"),
    path('ViewProduct/',sellerview.ViewProduct,name="ViewProduct"),
    path('edit<int:id>/',sellerview.edit,name="edit"),
    path('editAction/',sellerview.editAction,name="editAction"),
    path('delete<int:id>/',sellerview.delete,name="delete"),
    path('viewproduct_buy/',buyerview.viewproduct_buy,name="viewproduct_buy"),
    path('addtocart<int:id>/',buyerview.addtocart,name="addtocart"),
    path('addtocartAction/',buyerview.addtocartAction,name="addtocartAction"),
    path('Viewcart/',buyerview.Viewcart,name="Viewcart"),
    path('delete_cart<int:id>/',buyerview.delete_cart,name="delete_cart"),
    path('orderAction/',buyerview.orderAction,name="orderAction"),
    path('searchAction/',buyerview.searchAction,name="searchAction"),
    path('payment<int:id>/',buyerview.payment,name="payment"),
    path('payAction/',buyerview.payAction,name="payAction"),
    path('Vieworder/',buyerview.Vieworder,name="Vieworder"),
    path('details<int:id>/',buyerview.details,name="details"),
    path('CancelOrder<int:id>/',buyerview.CancelOrder,name="CancelOrder"),
    path('ViewOrder_seller/',sellerview.ViewOrder_seller,name="ViewOrder_seller"),
    path('details_seller<int:id>/',sellerview.details_seller,name="details_seller"),
    path('Approve_prdct<int:id>/',sellerview.Approve_prdct,name="Approve_prdct"),
    path('Reject_prdct<int:id>/',sellerview.Reject_prdct,name="Reject_prdct"),
    path('Confirmreject<int:id>/',sellerview.Confirmreject,name="Confirmreject"),
    path('Track<int:id>/',sellerview.Track,name="Track"),
    path('SendAction/',sellerview.SendAction,name="SendAction"),
    path('TrackingDetails<int:id>/',buyerview.TrackingDetails,name="TrackingDetails"),
    path('ResetPassword/',buyerview.ResetPassword,name="ResetPassword"),
    path('resetAction/',buyerview.resetAction,name="resetAction"),
    path('ResetPassword_seller/',sellerview.ResetPassword_seller,name="ResetPassword_seller"),
    path('resetAction_seller/',sellerview.resetAction_seller,name="resetAction_seller"),
    path('forgotpswd/',adminview.forgotpswd,name="forgotpswd"),
    path('nextAction/',adminview.nextAction,name="nextAction"),
    path('nextAction2/',adminview.nextAction2,name="nextAction2"), 
    path('resetAction_admin/',adminview.resetAction_admin,name="resetAction_admin"),
    path('logout/',sellerview.logout,name="logout"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)