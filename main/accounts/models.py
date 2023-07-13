import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def upload_image_formater(instance, filename):
	return f'{str(uuid.uuid4())}-{filename}'
class Cargo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cargo')
	class Meta:
		ordering = ('user',)

	def __str__(self):
		return '{} - {}'.format(self.user, self.cargo)

# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
	photo = models.ImageField('', upload_to=upload_image_formater, blank=True, null=True)
	phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
	birthday = models.DateField('Aniversário')

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.user.first_name)
