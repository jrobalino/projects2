from django.forms import ModelForm
from collection.models import SwimFace

class SwimFaceForm(ModelForm):
	class Meta:
		model = SwimFace
		fields = ('name', 'description')