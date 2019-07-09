from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .forms import AdvForm,ImageForm
from .models import Images,Advertisement,AdvTypes
from django.forms import modelformset_factory
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


@login_required
def add_advertise(request):
	if request.method=='POST':
		#import pdb; pdb.set_trace()

		form=AdvForm(request.POST)
		if form.is_valid():
			advertise=form.save(commit=False)
			advertise.user=request.user
			advertise.save()
			if request.FILES:
				save_images(request,advertise)
			return redirect('adv:show_adv', adv_id=advertise.id)
	else:                       
		return render(request, 'advertisements/add_advertise.html', {
		'form': AdvForm,
		})

@ensure_csrf_cookie
def save_adv_type(request,type):
	instance=AdvTypes(name=type)
	instance.save()
	data={'id':instance.id}
	return JsonResponse(data)



def save_images(request,advertise):
	#import pdb;pdb.set_trace()
	i=1
	images_list= request.FILES.getlist('image')
	for m in images_list:
		print(m)
		print('in request.files***********')
		instance=Images(image=m,order=i,advertisement=advertise)
		instance.save()
		i+=1
def delete_images(advertise):
	Images.objects.filter(advertisement=advertise).delete()

def show_adv(request,adv_id):
	is_the_adv_auth=False
	adv_obj = Advertisement.objects.get(pk=adv_id)
	#import pdb; pdb.set_trace()
	if request.user==adv_obj.user:
		is_the_adv_auth=True
	images_list=Images.objects.filter(advertisement=adv_obj).order_by("order")
	return render(request, 'advertisements/show_adv.html', {
		'adv': adv_obj,'imgs':images_list,
		'is_owner':is_the_adv_auth,
		})
def update_adv(request,adv_id):

	adv_obj = Advertisement.objects.get(pk=adv_id)

	if request.method =='POST':
		#import pdb;pdb.set_trace()

		form = AdvForm(request.POST,instance=adv_obj ,prefix='form1')
		if form.is_valid():
			form.save()
			images_list=Images.objects.filter(advertisement=adv_obj).order_by("order")
	
			ImagesFormSet=modelformset_factory(Images,form=ImageForm,fields=('image', ),extra=8-images_list.count(),can_delete=True)
			formset=ImagesFormSet(request.POST,request.FILES,prefix='form2')
			if images_list.count() == 0 :
				i=0
				for m, img in request.FILES.items():
					img=Images(image=img,advertisement=adv_obj,order=i)
					img.save()

				save_images(request,adv_obj)
			else:
				images = formset.save(commit=False)
				#import pdb;pdb.set_trace()	
				i=0
				for image in images:
					image.advertisement =adv_obj
					image.order=i
					image.save()
					i+=1
				for obj in formset.deleted_objects:
					obj.delete()

			return redirect('show_adv', adv_id=adv_obj.id)



	else:
		form=AdvForm(instance=adv_obj,prefix="form1")
		images_list=Images.objects.filter(advertisement=adv_obj).order_by("order")
		ImagesFormSet=modelformset_factory(Images,fields=('image', ),form=ImageForm,extra=8-images_list.count(),can_delete=True)
		#import pdb;pdb.set_trace()
		formsets=ImagesFormSet(queryset=Images.objects.filter(advertisement=adv_obj).order_by("order"),prefix="form2"
)
		return render(request, 'advertisements/update_adv.html', {
		'form': form,
		'images':images_list,
		'formsets':formsets,
		})


