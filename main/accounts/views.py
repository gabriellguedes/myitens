from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import *

# Novo Cliente(Cadastro Feito pelo próprio cliente)
def new_user(request):
	template_name='accounts/register.html'
	context={}
	if request.method == 'GET':
		form = UserRegistrationForm()
		
		context = {
			'form': form,
		}
		return render(request, template_name, context=context)
	elif request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		# Condição de tamanho da senha
		if len(request.POST['password']) < 6:
			context['msg'] = 'Senha deve conter no mínimo 6 caracteres.'
			context['class'] = 'alert alert-info'
			return render(request, template_name, context=context)
		#Validando Formulários
		if form.is_valid():
			try:
				new_user = form.save(commit=False)
				new_user.set_password(form.cleaned_data['password'])
				new_user.username = new_user.email				
				new_user.save()

				assign_role(new_user, 'cliente')
				user = authenticate(username=new_user.username, password=request.POST['password'])
				if user is not None:
					login(request, user)
					return HttpResponseRedirect(reverse('accounts:cliente_detail', kwargs={'pk': new_user.id}))
				else:
					form = UserRegistrationForm()
					context = {
						'form': form,
						'msg': 'Algo deu errado!',
						'class': 'alert alert-primary',
					}
					return render(request, template_name, context=context)
			except IntegrityError:
				form = UserRegistrationForm()
				context = {
					'form': form,
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
# Detail Cliente acesso pelo cliente
def user_detail(request, pk):
	template_name = 'accounts/user_detail.html'
	user = request.user
	context = {
		'user': user,
	}
	return render(request, template_name, context=context)
# Atualização Cliente Feita pelo Cliente
def user_update(request, pk):
    template_name = 'accounts/user_update.html'
    if request.user.is_authenticated:
    	user = request.user

    obj = User.objects.get(id=pk)
   
    try:
        cliente =  Profile.objects.get(user=obj)
        if cliente != None:
            a = 0
        else:
            a = 1
    except ObjectDoesNotExist:
        a = 1

    try:
        endereco = Endereco.objects.get(user=obj)
        if  endereco != None:
            b = 0 
        else:
            b = 1
    except ObjectDoesNotExist:
        b =1   


    if request.method == 'GET':
    	user_form = UserEditForm(instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateForm, extra=a, can_delete=False)
    	form_cliente = form_cliente_factory(instance=obj)
    	form_endereco_factory = inlineformset_factory(User, Endereco, form=EnderecoForm, extra=b, can_delete=False)
    	form_endereco = form_endereco_factory(instance=obj)

    	context = {
    		'user_form': user_form,
    		'profile_form': form_cliente,
    		'endereco': form_endereco,
    		'cliente': obj,
    		
    	}
    	return render(request, template_name, context=context)
    elif request.method == 'POST':
    	user_form = UserEditForm(request.POST,instance=obj)
    	form_cliente_factory = inlineformset_factory(User, Profile, form=ProfileUpdateForm, can_delete=False)
    	form_cliente = form_cliente_factory(request.POST, request.FILES, instance=obj)
    	form_endereco_factory = inlineformset_factory(User, Endereco, form=EnderecoForm, extra=a, can_delete=False)
    	form_endereco = form_endereco_factory(request.POST ,instance=obj)

    	if user_form.is_valid() and form_cliente.is_valid() and form_endereco.is_valid():
    		edit_user = user_form.save(commit=False)
    		form_cliente.instance = edit_user 
    		edit_user.save()
    		form_cliente.save()
    		form_endereco.save()
    		return HttpResponseRedirect(reverse('contas:cliente_detail', kwargs={'pk': pk}))
    	else:
    		context = {
    			'user_form': user_form,
    			'profile_form': form_cliente,
    			'endereco': form_endereco,
    			'cliente': obj,
    			
    		}
    		return render(request,  template_name, context=context)
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

