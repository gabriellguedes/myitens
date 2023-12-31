import os
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')

	def upload_image_formater(self, instance, filename):
		user = self.user.username
		return f'{user}/{str(uuid.uuid4())}-{filename}'

	photoProfile = models.ImageField('', upload_to=upload_image_formater, blank=True, null=True)
	photoCapa = models.ImageField('', upload_to=upload_image_formater, blank=True, null=True)
	phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
	birthday = models.DateField('Aniversario', blank=True, null=True)
	bio = models.TextField('Bio', max_length=200, blank=True, null=True)
	created = models.DateTimeField( 'criado_em', auto_now_add=True, auto_now=False)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.user.first_name)
