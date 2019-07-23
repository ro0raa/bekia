from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from advertisements.models import  Advertisement,Images
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	adv_list=Advertisement.objects.all().order_by('-created')
	images=Images.objects.filter(order=1)
	dict={}

	for obj in adv_list:
		image=None
		for m in images:
			print(m.advertisement.id)
			if obj.id==m.advertisement.id:
				image=m.image
		dict.update({obj:image})

	page = request.GET.get('page', 1)
	t = tuple(dict.items())

	paginator = Paginator(t, 6)
	try:
		advs = paginator.page(page)
	except PageNotAnInteger:
		advs = paginator.page(1)
	except EmptyPage:
		advs = paginator.page(paginator.num_pages)

	return render(request, 'index.html',{'advs':advs,})




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


@login_required
def dashboard(request):
	adv_list=Advertisement.objects.filter(user=request.user)
	context={
				'advs': adv_list,
    		}
	return render(request, 'dashboard.html',context)

