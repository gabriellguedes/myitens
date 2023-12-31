from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from main.core.views import newsletter_add
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import UserProfile
from .forms import *
from main.gallery.forms import PhotoForm

# Login no App
def user_login(request):
	template_name = "registration/login.html"
	if request.method == 'GET':
		form = LoginForm()
		context = {
			'form': form
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = LoginForm(request.POST or None)
		context = {
			"form": form
		}
		if form.is_valid():
			username = request.POST["username"]
			password = form.cleaned_data.get("password")
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse( 'core:home'))
			else:
				context = {'msg': 'Algo deu errado!'}
				return render(request, template_name, context=context)

#	Criando um novo usuário, perfil e adicionando-o a lista de emails.
#	(Cadastro realizado pelo próprio cliente)
def new_user(request):
	template_name='accounts/register.html'
	context={}
	if request.method == 'GET':
		form = UserRegistrationForm()
		form_profile_factory = inlineformset_factory(User, UserProfile, form=UserProfileForm, extra=1, can_delete=False)
		form_user = form_profile_factory()
		context = {
			'form': form,
			'form_user': form_user,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		form_profile_factory = inlineformset_factory(User, UserProfile, form=UserProfileForm, extra=0, can_delete=False)
		form_user = form_profile_factory(request.POST)
		# Condição de tamanho da senha
		if len(request.POST['password']) < 6:
			context['msg'] = 'Senha deve conter no mínimo 6 caracteres.'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		#Validando Formulários
		if form.is_valid() and form_user.is_valid():
			try:
				new_user = form.save(commit=False)
				new_user.set_password(form.cleaned_data['password'])
				new_user.username =  new_user.first_name
				new_user.save()
				form_user.instance = new_user
				form_user.save()
				#Verificando se o perfil do Usuário foi criado e vinculado ao usuário.	
				try:
					profile = UserProfile.objects.get(user=new_user)
				except ObjectDoesNotExist:	
					profile = UserProfile.objects.create(user=new_user)
				# Adicionando usuário a lista de email	
				if request.POST.get('email_market', False):
					nome = new_user.first_name
					email = new_user.email
					newsletter_add(nome, email)
				else:
					pass	
					
				# Realizando o login apoś a criação do usuário e perfil	
				user = authenticate(username=new_user.username, password=request.POST['password'])
				if user is not None:
					login(request, user)
					return HttpResponseRedirect(reverse('core:user_profile', kwargs={'pk': new_user.username}))
				else:
					form = UserRegistrationForm()
					context = {
						'form': form,
						'form_user': form_user,
						'msg': 'Algo deu errado!',
						'class': 'alert alert-primary',
					}
					return render(request, template_name, context=context)
			except IntegrityError:
				form = UserRegistrationForm()
				context = {
					'form': form,
					'form_user': form_user,
					'msg': 'Email já cadastrado.',
					'class': 'alert alert-warning',
				}
				return render(request, template_name, context=context)
		else:
			context = {
				'form': form,
				'msg': 'Usuário não foi cadastrado!',
				'class': 'alert alert-warning',
			}
			return render(request, template_name, context=context)
# Detail Cliente acesso pelo cliente
def user_profile(request, pk):
	template_name = 'accounts/user_detail.html'
	user = User.objects.get(username=pk)
	profile = UserProfile.objects.get(user=user)

	# Atualizar a biografia 
	if request.method == "GET":
		updateBio = BioUpdateForm(instance=profile)
		updatePhoto = PhotoUpdateForm(instance=profile)
		updateCover = CoverUpdateForm(instance=profile)
		user_form = UserEditForm(instance=user)
		profile_form_factory = inlineformset_factory(User, UserProfile, form=UserProfileEditForm, extra=0, can_delete=False)
		form_profile = profile_form_factory(instance=user)
		photo = PhotoForm(instance=profile)

		context = {
			'user': user,
			'profile': profile,
			'form_bio': updateBio,
			'form_photo': updatePhoto,
			'form_cover': updateCover,
			'user_form': user_form,
			'photo': photo,
    	 	'profile_form': form_profile,
		}
		return render(request, template_name, context=context)
	
	context = {
		'user': user,
		'profile': profile,
	}
	return render(request, template_name, context=context)
# Editar a biografia
def edit_bio(request, pk):
	template_name = 'accounts/profile/edit_bio.html'
	user = User.objects.get(id=pk)
	profile = UserProfile.objects.get(user=user)
	
	# Atualizar a biografia 
	if request.method=="POST":
		updateBio = BioUpdateForm(request.POST, instance=profile)
		if updateBio.is_valid():
			new_bio = updateBio.save(commit=False)
			new_bio.save()
			return HttpResponseRedirect(reverse('core:user_profile', kwargs={'pk': user.username}))
		else:	
			context = {
			'user': user,
			'profile': profile,
			'form_bio': updateBio,
			'msg': "Formulário não é válido",
		}
		return render(request, template_name, context=context)
# Atualização Cliente Feita pelo Cliente
def edit_profile(request, pk):
    template_name = 'accounts/profile/edit_profile.html'
    user = User.objects.get(id=pk)
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=user)
    	profile_form_factory = inlineformset_factory(User, UserProfile, form=UserProfileEditForm, can_delete=False)
    	form_profile = profile_form_factory(request.POST, request.FILES, instance=user)
    	if user_form.is_valid() and form_profile.is_valid():
    		edit_user = user_form.save(commit=False)
    		edit_user.save()
    		form_profile.instance = edit_user
    		form_profile.save()
    		return HttpResponseRedirect(reverse('core:home'))
    		#return HttpResponseRedirect(reverse('accounts:user_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    		 'user_form': user_form,
    		 'profile_form': form_profile,
    		 'user': user,
    		 'profile': profile,
    		}
    		return render(request,  template_name, context=context)
# Listar Todos os Clientes Cadastrados no Sistema
def user_list(request):
	template_name = 'accounts/user_list.html'
	if request.user.is_authenticated:
		user = request.user
	else:
		user = ''

	obj_users = User.objects.all()

	parametro_page = request.GET.get('page', '1')
	parametro_limit = request.GET.get('limit', '5')

	if not (parametro_limit.isdigit() and int(parametro_limit)>0):
		parametro_limit = '10'

	clientes = User.objects.get_queryset().order_by('id')
	clientes_paginator = Paginator(clientes, parametro_limit)

	lista = User.objects.all()
	profile = Profile.objects.all()
	try:
		page = clientes_paginator.page(parametro_page)

	except (EmptyPage, PageNotAnInteger):
		page = clientes_paginator.page(1)


	context = {
		'items_list': ['5','10', '20', '30', '50'],
        'qnt_page':parametro_limit,
        'clientes': page,
		'lista': lista,
		'user': user,
		'profile': profile,
	}
	return render(request, template_name, context=context)
#Apagar Cliente   
def user_delete(request, pk):
	template_name = 'accounts/user_delete.html'
	objeto = User.objects.get(id=pk)
	if request.method == 'GET':
		context = {'cliente': objeto,}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		objeto.delete()
		return HttpResponseRedirect(reverse('contas:cliente_list'))




