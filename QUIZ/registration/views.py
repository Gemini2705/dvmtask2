from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import usertype

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		
		if form.is_valid():
			form.save()
			
			messages.success(request, f'Your Account Has Been Created. You Can Now Login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form': form})

