from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'index.html',{})




@login_required
def profile(request):

	user = User.objects.get(id=request.user.id)
	if request.method =='POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		
		if u_form.is_valid() :
			u_form.save()
		
		messages.success(request, f'Yout Account successfully Updated')
		return redirect('/')
	else:
		u_form = UserUpdateForm(instance=request.user)
		


	context={
			'user_update': u_form,
			
			}
	return render(request, 'users/profile.html', context)