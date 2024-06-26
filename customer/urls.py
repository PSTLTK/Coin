"""
URL configuration for Coin project.

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
from django.urls import path
from customer import views,randomviews

app_name = "customer"

urlpatterns = [
    path('get_qr_link/', views.GetQRLink),
    path('withdraw/',views.Withdraw),
    path('account/',views.Account),
    path('deposit/',views.Deposit),
    path('room/',views.RoomChoice),
    path('random/',randomviews.RandomCreate,name="randomc"),
    path('new_member/',views.NewMember),
    path('intermediate/',views.Intermediate),
    path('advanced/',views.Advanced),
    path('viproom/',views.Vip),
    path('upick/<str:uc>/<str:am>/<str:rm>/',randomviews.UserChoice),
    path('uhistroy/',randomviews.UserChoiceHistroy),
    path('deposit_bonus/',views.DepositBonus),
    path('market/',views.Market),
]
