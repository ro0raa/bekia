from django.shortcuts import render ,redirect
 
from .forms import AdvForm
from .models import Images

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
			return redirect('/')
	else:        				
		return render(request, 'advertisements/add_advertise.html', {
        'form': AdvForm,
    	})
def save_images(request,advertise):
	i=1
	images_list= request.FILES.getlist('image')
	for m in images_list:
		instance=Images(image=m,order=i,advertisement=advertise)
		instance.save()
		i+=1


	print(advertise)
