from django.shortcuts import render
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