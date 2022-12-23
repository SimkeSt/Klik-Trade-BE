from django.urls import path, include
from . import views
urlpatterns = [

 path('',views.home, name = "home"),
 path('<int:rid>',views.afilliategetter, name='kuki'),  
 path('paypal-return/', views.PaypalReturnView.as_view(), name='paypal-return'),
 path('paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
 path("signup/", views.SignUp.as_view(), name="signup"),
 path('cryptodata/', views.cryptodata, name='cryptodata'),
 path('stockdata/', views.stockdata, name='stockdata'),
 path('plati', views.plati, name='plati'),
 path(r'^paypal/', include('paypal.standard.ipn.urls')),

 path('profile/', views.profile, name='profile'),
 #path('scookie/<int:rid>',views.afilliategetter, name='kuki'),  
 path('gcookie',views.getcookie),
 path('thank_you', views.collectinfo, name="thank_you"),


  
  
]