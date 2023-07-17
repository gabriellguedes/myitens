import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def upload_image_formater(instance, filename):
	return f'{str(uuid.uuid4())}-{filename}'

# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
	photoProfile = models.ImageField('', upload_to=upload_image_formater, blank=False, null=False)
	photoCapa = models.ImageField('', upload_to=upload_image_formater, blank=False, null=False)
	phone = models.CharField('Telefone', max_length=16, blank=False, null=False)
	birthday = models.DateField('Aniversário', blank=False, null=False, auto_now_add=True)
	bio = models.TextField('Bio', max_length=200, blank=False, null=False)
	created = models.DateTimeField( 'criado_em', auto_now_add=True, auto_now=False)

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.user.first_name)
