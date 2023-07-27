from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Imagem
import os

@receiver(pre_delete, sender=Imagem)
def pre_delete_imagem(sender, instance, **kwargs):
    os.remove(instance.original.path)
