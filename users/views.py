#users/views.py

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


# Create your views here.
 
def home(request):
  return render(request,"users/home.html")



class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


def cryptodata(request):
  return render(request,"users/cryptodata.html")


def stockdata(request):
  return render(request,"users/stockdata.html")


def plati(request):
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