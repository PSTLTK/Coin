from django.shortcuts import render,redirect
import random
from customer.models import *
from account.models import User
from django.http import HttpResponse

def RandomCreate(request):
    a1 = random.randint(1,10)
    b1 = random.randint(1,10)
    c1 = random.randint(1,10)
    r1 = RandomModel.objects.filter(room=1).last()
    ran = RandomModel.objects.create(
        a = a1,
        b = b1,
        c = c1,
        room = 1,
        status = "free",
        roundno = int(str(r1.roundno)) + 1,
        total = a1 + b1 + c1
        )
    ran.save()

    a2 = random.randint(1,10)
    b2 = random.randint(1,10)
    c2 = random.randint(1,10)
    r2 = RandomModel.objects.filter(room=2).last()
    ran = RandomModel.objects.create(
        a = a2,
        b = b2,
        c = c2,
        room = 2,
        status = "free",
        roundno = int(str(r2.roundno)) + 1,
        total = a2 + b2 + c2
        )
    ran.save()

    a3 = random.randint(1,10)
    b3 = random.randint(1,10)
    c3 = random.randint(1,10)
    r3 = RandomModel.objects.filter(room=3).last()
    ran = RandomModel.objects.create(
        a = a3,
        b = b3,
        c = c3,
        room = 3,
        status = "free",
        roundno = int(str(r3.roundno)) + 1,
        total = a3 + b3 + c3
        )
    ran.save()

    a4 = random.randint(1,10)
    b4 = random.randint(1,10)
    c4 = random.randint(1,10)
    r4 = RandomModel.objects.filter(room=4).last()
    ran = RandomModel.objects.create(
        a = a4,
        b = b4,
        c = c4,
        room = 4,
        status = "free",
        roundno = int(str(r4.roundno)) + 1,
        total = a4 + b4 + c4
        )
    ran.save()

    UserResult1()
    UserResult2()
    UserResult3()
    UserResult4()

    ranu1 = RandomModel.objects.get(status="now",room=1)
    ranu1.status = "used"
    ranu1.save()
    
    rann1 = RandomModel.objects.filter(status="free",room=1).first()
    rann1.status = "now"
    rann1.save()

    ranu2 = RandomModel.objects.get(status="now",room=2)
    ranu2.status = "used"
    ranu2.save()
    
    rann2 = RandomModel.objects.filter(status="free",room=2).first()
    rann2.status = "now"
    rann2.save()

    ranu3 = RandomModel.objects.get(status="now",room=3)
    ranu3.status = "used"
    ranu3.save()
    
    rann3 = RandomModel.objects.filter(status="free",room=3).first()
    rann3.status = "now"
    rann3.save()

    ranu4 = RandomModel.objects.get(status="now",room=4)
    ranu4.status = "used"
    ranu4.save()
    
    rann4 = RandomModel.objects.filter(status="free",room=4).first()
    rann4.status = "now"
    rann4.save()

    pass

def UserChoice(request,uc,am,rm):
    current_user = User.objects.get(email = request.user.email)
    ran = RandomModel.objects.get(status="now",room=rm)
    uc = UserChoiceModel.objects.create(
            choice = uc,
            amount = am,
            room = rm,
            roundno = ran.roundno,
            user = current_user
        )
    uc.save()
    coin = CoinModel.objects.get(customer=uc.user.id)
    coin.quantity =  coin.quantity - int(uc.amount)
    coin.save()
    url = '/'
    if rm == '1':
        url = '/customer/new_member/'
    elif rm == '2':
        url = '/customer/intermediate/'
    elif rm == '3':
        url = '/customer/advanced/'
    elif rm == '4':
        url = '/customer/viproom/'
    return redirect(url)
    
    

def UserChoiceHistroy(request):
    current_user = User.objects.get(email = request.user.email)
    uc = UserChoiceModel.objects.filter(user=current_user)
    return render(request,'userhistroy.html',{"uc":uc})

def UserResult1():
    ran = RandomModel.objects.get(status="now",room=1)
    if ran.total <= 13:
        bb = "bear"
    else:
        bb = "bull"

    if ran.total % 2 ==0:
        ts = "twin"
    else:
        ts = "single"

    ucs = UserChoiceModel.objects.filter(roundno=ran.roundno,result="pending")
    for uc in ucs:
        if uc.choice == bb or uc.choice == ts:
            win = uc.amount * 0.9
            coin = CoinModel.objects.get(customer=uc.user.id)
            coin.quantity =  coin.quantity + win
            coin.save()
            uc.result = "success"
            uc.save()
        else:
            uc.result = "failed"
            uc.save()


def UserResult2():
    ran = RandomModel.objects.get(status="now",room=2)
    if ran.total <= 13:
        bb = "bear"
    else:
        bb = "bull"

    if ran.total % 2 ==0:
        ts = "twin"
    else:
        ts = "single"

    ucs = UserChoiceModel.objects.filter(roundno=ran.roundno,result="pending")
    for uc in ucs:
        if uc.choice == bb or uc.choice == ts:
            win = uc.amount * 0.9
            coin = CoinModel.objects.get(customer=uc.user.id)
            coin.quantity =  coin.quantity + win
            coin.save()
            uc.result = "success"
            uc.save()
        else:
            uc.result = "failed"
            uc.save()


def UserResult3():
    ran = RandomModel.objects.get(status="now",room=3)
    if ran.total <= 13:
        bb = "bear"
    else:
        bb = "bull"

    if ran.total % 2 ==0:
        ts = "twin"
    else:
        ts = "single"

    ucs = UserChoiceModel.objects.filter(roundno=ran.roundno,result="pending")
    for uc in ucs:
        if uc.choice == bb or uc.choice == ts:
            win = uc.amount * 0.9
            coin = CoinModel.objects.get(customer=uc.user.id)
            coin.quantity =  coin.quantity + win
            coin.save()
            uc.result = "success"
            uc.save()
        else:
            uc.result = "failed"
            uc.save()

def UserResult4():
    ran = RandomModel.objects.get(status="now",room=4)
    if ran.total <= 13:
        bb = "bear"
    else:
        bb = "bull"

    if ran.total % 2 ==0:
        ts = "twin"
    else:
        ts = "single"

    ucs = UserChoiceModel.objects.filter(roundno=ran.roundno,result="pending")
    for uc in ucs:
        if uc.choice == bb or uc.choice == ts:
            win = uc.amount * 0.9
            coin = CoinModel.objects.get(customer=uc.user.id)
            coin.quantity =  coin.quantity + win
            coin.save()
            uc.result = "success"
            uc.save()
        else:
            uc.result = "failed"
            uc.save()