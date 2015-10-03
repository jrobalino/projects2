from django.shortcuts import render, redirect
from collection.forms import SwimFaceForm
from collection.models import SwimFace
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
	number = 7
	swimfaces = SwimFace.objects.all()
	swimfacesFiltered = SwimFace.objects.filter(description__contains='Egyptian')
	return render(request, 'index.html', { 'number': number, 'swimfaces': swimfaces, 'swimfacesFiltered': swimfacesFiltered})

def swimface_detail(request, slug):
	swimface = SwimFace.objects.get(slug=slug)
	return render(request, 'swimfaces/swimface_detail.html', { 'swimface': swimface,})

@login_required
def edit_swimface(request, slug):
	swimface = SwimFace.objects.get(slug=slug)
	if swimface.user != request.user:
		raise Http404

	form_class=SwimFaceForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=swimface)
		if form.is_valid():
			form.save()
			return redirect('swimface_detail', slug=swimface.slug)
	else:
		form = form_class(instance=swimface)

	return render(request, 'swimfaces/edit_swimface.html', {'swimface': swimface, 'form': form, })

def create_swimface(request):
	form_class = SwimFaceForm
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			swimface = form.save(commit=False)
			swimface.user = request.user
			swimface.slug = slugify(swimface.name)
			swimface.save()
			return redirect('swimface_detail', slug=swimface.slug)
	else:
		form = form_class()
	return render(request, 'swimfaces/create_swimface.html', {
		'form': form,
	})

def browse_by_name(request, initial=None):
	if initial:
		swimfaces = SwimFace.objects.filter(name__istartswith=initial).order_by('name')

	else:
		swimfaces = SwimFace.objects.all().order_by('name')

	return render(request, 'search/search.html', {
		'swimfaces': swimfaces,
		'initial': initial,
	})