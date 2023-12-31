
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import UserProfile
from main.core.forms import DateInput
from django.contrib.auth import get_user_model

#Login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Criar um no perfil de usuário
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
		widgets = {'birthday': DateInput()}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['phone'].widget.attrs.update({'class':'mask-phone'})

# Atualização dos dados do perfil Feita pelo cliente
class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthday', 'phone',)
        widgets = {'birthday': DateInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class':'mask-phone'})

# Atualizar a capa 
class CoverUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('photoCapa',)

# Atualizar do Perfil 
class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('photoProfile',)

#Atualizar a Biografia
class BioUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio',)

# Cadastro de um novo Usuário 
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(),
        )
    first_name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ('first_name', 'email')

    def clean_first_name(self):
        nome = self.cleaned_data['first_name']
        if nome == '' or nome == None:
            raise ValidationError("O campo Nome deve ser preenchido!")
        else:
            return nome

    def clean_email(self):
        email = self.cleaned_data['email']
        if email =='':
            raise ValidationError("O campo email deve ser preenchido!")
        else:
            return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise ValidationError("Insira uma senha.")
        elif len(password) < 6:
            raise ValidationError("Mínimo de 6 caracteres.")

        else:
            return password

# Editar Usuário no Sistema
class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ('first_name', 'email')

#teste
class NewProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'phone', 'birthday', )
        widgets = {'birthday': DateInput()}
