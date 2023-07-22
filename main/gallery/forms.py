from django import forms
from .models import Album, Imagem
from croppie.fields import CroppieField

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = '__all__'

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Imagem
		fields = '__all__'
