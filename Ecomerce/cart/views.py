from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from home.models import *
from .models import *


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

@login_required(login_url='login')
def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    user = request.user
    try:
        ct = cartlist.objects.get(user=user)
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request), user=user)
        ct.save()
    try:
        c_item = items.objects.get(prod=prod, cart=ct)
        if c_item.quan < c_item.prod.stock:
            c_item.quan += 1
            prod.stock -= 1
            prod.save()
        c_item.save()
    except items.DoesNotExist:
        c_item = items.objects.create(prod=prod, quan=1, cart=ct)
        prod.stock -= 1
        prod.save()
        c_item.save()
    return redirect('cart')


# Create your views here.
def cart(request, tot=0, count=0, cart_item=None, ct_item=None):
    try:
        user = request.user
        if user.is_authenticated:
            ct = cartlist.objects.filter(user=user)
        else:
            cart_id = request.session.get('cart_id')
            ct = cartlist.objects.filter(cart_id=cart_id)
        ct_items = items.objects.filter(cart__in=ct, active=True)

        for i in ct_items:
            tot += (i.prod.price * i.quan)
            count += i.quan

    except ObjectDoesNotExist:
        return HttpResponse("<script> alert('Empty Cart');window.location='/';</script>")

    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


@login_required(login_url='login')
def minus_cart(request, product_id):
    user = request.user
    try:
        if user.is_authenticated:
            ct_list = cartlist.objects.filter(user=user)
        else:
            cart_id = request.session.get('cart_id')
            ct_list = cartlist.objects.filter(cart_id=cart_id)
        if ct_list.exists:
            for ct in ct_list:
                pro = get_object_or_404(product,id=product_id)
                try:
                    c_items =items.objects.get(prod=pro,cart=ct)
                    if c_items.quan > 1:
                        c_items.quan -= 1
                        c_items.save()
                    else:
                        c_items.delete()
                except items.DoesNotExist:
                    pass
    except items.DoesNotExist:
        pass
    return redirect('cart')

@login_required(login_url='login')
def cart_delete(request, product_id):
    user = request.user
    try:
        if user.is_authenticated:
            ct_list = cartlist.objects.filter(user=user)
        else:
            cart_id = request.session.get('cart_id')
            ct_list = cartlist.objects.filter(cart_id=cart_id)
        if ct_list.exists:
            for ct in ct_list:
                prod = get_object_or_404(product,id=product_id)
                try:
                    c_items =items.objects.get(prod=prod, cart=ct)
                    c_items.delete()

                except items.DoesNotExist:
                    pass
    except items.DoesNotExist:
        pass
    return redirect('cart')
def checkout(request):
    if request.method =='POST':
        firstname= request.POST["fname"]
        lastname = request.POST["lname"]
        country = request.POST["country"]
        state = request.POST["state"]
        address = request.POST["address"]
        towncity =request.POST["city"]
        postcodezip= request.POST["pin"]
        phone = request.POST["Phone"]
        email = request.POST["email"]
        cart = cartlist.objects.filter(user=request.user).first()

        check = billing(
            user=request.user,
            cart=cart,
            firstname=firstname,
            lastname=lastname,
            country=country,
            state=state,
            address=address,
            town=towncity,
            postcode=postcodezip,
            phone=phone,
            email=email
        )
        check.save()
        return redirect('bankform')
    return render(request, 'checkout.html')
def Bankform(request):
    if request.method =='POST':
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        account = request.POST["account"]
        Expiry_date = request.POST["Expiry_date"]
        upto = request.POST["upto"]
        cvv = request.POST["cvv"]

        bank = bankform(
            user=request.user,
            firstname=firstname,
            lastname=lastname,
            accountno=account,
            cvv=cvv,
            expiryFrom=Expiry_date,
            upto=upto
        )
        bank.save()
        return redirect('index')

    return render(request,'bankform.html')