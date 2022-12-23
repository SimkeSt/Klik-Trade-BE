#users/views.py

from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.template import loader

from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from .models import Profile

from django.shortcuts import redirect
from django.contrib import messages

from django.contrib import messages
from django.conf import settings
from django.views.generic import FormView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.generic import TemplateView

def collectinfo(request):
    return render(request,"/users/thank_you.html")

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'

class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'

class PaypalFormView(FormView):
    template_name = 'paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        return {
            "business": 'your-paypal-business-address@example.com',
            "amount": 20,
            "currency_code": "EUR",
            "item_name": 'Example item',
            "invoice": 1234,
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }

 
def home(request):
  return render(request,"users/home.html")



class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


def cryptodata(request):
    import pandas as pd

    df=pd.read_csv('test8.csv')
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'users/cryptodata.html', context=mydict)


def paypal(request):
  return render(request,"users/paypal.html")


def stockdata(request):
  return render(request,"users/stockdata.html")


def plati(request):
  if "ID" in request.COOKIES.keys():
    refid  = request.COOKIES['ID']  
    request.user.referent = refid
    return render(request,"users/plati.html")
  else: 
    return render(request,"users/plati.html")


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.hobby = 'Coding, Chess, Guitar'
    user.save()

def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Profile has been Updated Successfully')
			return redirect('profile')
	else:	
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		context = {
			'u_form': u_form,
			'p_form': p_form
		}
	return render(request, 'users/profile.html', context)

def afilliategetter(request,rid):  
    response = render(request,"users/home.html")
    response.set_cookie('ID', rid)  
    return response  
	


def getcookie(request):  
    refid  = request.COOKIES['ID']  
    return HttpResponse("ID: "+  refid);  
