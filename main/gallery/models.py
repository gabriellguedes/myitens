from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

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
        upload_to='galeria/original',
        )

    publicacao = models.DateTimeField(auto_now_add=True, auto_now=False)

