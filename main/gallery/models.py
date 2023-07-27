import os
import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

def upload_image_formater(instance, filename):
    try:
        user = instance.user.photo.all()
        for i in user:
            folder = i.album.titulo
        return '{}/{}/{}'.format(instance.user.username, folder,{str(uuid.uuid4())}-{filename})
    except UnboundLocalError:
        return '{}/except/{}'.format(instance.user.username, {str(uuid.uuid4())}-{filename})

class Album(models.Model):
    class Meta:
        ordering = ('titulo',)
        
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Imagem(models.Model):
    
    class Meta:
        ordering = ('publicacao',)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='gallery')
    original = models.ImageField(
        null=True,
        blank=True,
        upload_to=upload_image_formater,
        )

    publicacao = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.album.titulo)
