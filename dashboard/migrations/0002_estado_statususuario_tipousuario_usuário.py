# Generated by Django 5.1.3 on 2025-01-21 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='StatusUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuário',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=128)),
                ('data_cadastro', models.DateField(auto_now=True)),
                ('rua', models.CharField(max_length=35)),
                ('bairro', models.CharField(max_length=35)),
                ('cidade', models.CharField(max_length=35)),
                ('cep', models.CharField(max_length=15)),
                ('imagem', models.ImageField(default='static/img/img_perfil.jpg', upload_to='imagens/usuario')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.estado')),
                ('status_usuario', models.ForeignKey(default='indefinido', on_delete=django.db.models.deletion.SET_DEFAULT, to='dashboard.statususuario')),
                ('tipo_usuario', models.ForeignKey(default='indefinido', on_delete=django.db.models.deletion.SET_DEFAULT, to='dashboard.tipousuario')),
            ],
        ),
    ]
