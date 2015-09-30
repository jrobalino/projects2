from django.shortcuts import render

# Create your views here.
def index(request):
	number = 7
	thing = "Swim Faces"
	return render(request, 'index.html', { 'number': number, 'thing': thing})