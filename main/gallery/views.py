from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from main.accounts.models import UserProfile
from .models import Imagem, Album
from .forms import AlbumForm, PhotoForm
from main.accounts.forms import UserRegistrationForm

# Create your views here.
def createAlbum(request):
	template_name='gallery/creategallery.html'

	if request.method == 'GET':
		form = AlbumForm()
		context = {'form': form,}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = AlbumForm(request.POST)
		if form.is_valid():
			new_gallery = form.save(commit=False)
			new_gallery.save()
			return HttpResponseRedirect(reverse('gallery:new_gallery'))
		else:
			context = {
				'msg':'Algo deu errado!'
			}	
			return render(request, template_name, context=context)

# Adicionando uma nova foto ao Perfil
def photo(request, pk):
	template_name='accounts/profile/photo.html'
	user = User.objects.get(id=pk)
	album = Album.objects.get(id=1)

	if request.method == 'GET':
		album_form = AlbumForm(instance=album)
		img_form_factory = inlineformset_factory(Album, Imagem, form=PhotoForm, extra=1, can_delete=False)
		form_img = img_form_factory()

		context = {
			'form_profile': album_form,
			'photo': form_img,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':			
		album_form = AlbumForm(request.POST)
		img_form_factory = inlineformset_factory(Album, Imagem, form=PhotoForm)
		form_img = img_form_factory(request.POST, request.FILES)
		
		if form_img.is_valid():
			new_photo = form_img.save(commit=False)
			form_img.instance = album
			new_photo[0].user = user
			form_img.save()

			return HttpResponseRedirect(reverse('accounts:user_profile', kwargs={'pk':pk}))
		else:	
			context = {
			'form_profile': album_form,
			'photo': form_img,
			}
			return render(request, template_name, context=context)

# Adicionando uma nova foto de capa
def cover(request, pk):
	template_name='accounts/profile/cover.html'
	user = User.objects.get(id=pk)
	cover = Album.objects.get(id=2)

	if request.method == 'GET':
		form = AlbumForm()
		cover_form_factory = inlineformset_factory(Album, Imagem, form=PhotoForm, extra=1, can_delete=False)
		form_cover = cover_form_factory()

		context={
			'cover': form_cover,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = AlbumForm(request.POST)
		cover_form_factory = inlineformset_factory(Album, Imagem, form=PhotoForm, extra=1, can_delete=False)
		form_cover = cover_form_factory(request.POST, request.FILES)

		if form_cover.is_valid():
			new_cover = form_cover.save(commit=False)
			form_cover.instance = cover
			form_cover.save()

			return HttpResponseRedirect(reverse('accounts:user_profile', kwargs={'pk':pk}))
		else:
			context={
				'cover':form_cover,
			}
			return render(request, template_name, context=context)

		


# Alterar a foto de perfil por uma que está no Album
def selectPhoto(request, pk):
	photo = Imagem.objects.filter(id=pk)
	last = Imagem.objects.last()
	owner = photo.user
	if request.user == owner:
		for fields in photo:
			url = fields.url
			pk = fields.id
			if last.id != fields.id:
				pass
	
	context = {
		'photo.url':url,
	}		
	return render(request, context=context)