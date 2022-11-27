from django.urls import path
from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path("signup/", views.SignUp.as_view(), name="signup"),
 path('cryptodata/', views.cryptodata, name='cryptodata'),
 path('stockdata/', views.stockdata, name='stockdata'),
 path('plati/', views.plati, name='plati'),
 path('profile/', views.profile, name='profile')

]