# Generated by Django 4.2.3 on 2023-07-16 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.accounts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoProfile', models.ImageField(upload_to=main.accounts.models.upload_image_formater, verbose_name='')),
                ('photoCapa', models.ImageField(upload_to=main.accounts.models.upload_image_formater, verbose_name='')),
                ('phone', models.CharField(max_length=16, verbose_name='Telefone')),
                ('birthday', models.DateField(verbose_name='Aniversário')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado_em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
