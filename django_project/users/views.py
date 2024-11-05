from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm 

def register(requests) :
	if requests.method == 'POST' :
		form = UserRegisterForm(requests.POST)
		if form.is_valid() :
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(requests, f'Account created for {username}!')
			return redirect('blog-home')
	else :
		form = UserRegisterForm()
	return render(requests, 'users/register.html', {'form' : form})
