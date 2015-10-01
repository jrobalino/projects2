from django.shortcuts import render, redirect
from collection.forms import SwimFaceForm
from collection.models import SwimFace

# Create your views here.
def index(request):
	number = 7
	swimfaces = SwimFace.objects.all()
	swimfacesFiltered = SwimFace.objects.filter(description__contains='Egyptian')
	return render(request, 'index.html', { 'number': number, 'swimfaces': swimfaces, 'swimfacesFiltered': swimfacesFiltered})

def swimface_detail(request, slug):
	swimface = SwimFace.objects.get(slug=slug)
	return render(request, 'swimfaces/swimface_detail.html', { 'swimface': swimface,})

def edit_swimface(request, slug):
	swimface = SwimFace.objects.get(slug=slug)
	form_class=SwimFaceForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=swimface)
		if form.is_valid():
			form.save()
			return redirect('swimface_detail', slug=swimface.slug)
	else:
		form = form_class(instance=swimface)

	return render(request, 'swimfaces/edit_swimface.html', {'swimface': swimface, 'form': form, })