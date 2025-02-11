# Generated by Django 5.1.4 on 2025-02-11 20:18

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='Forma_Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pagamento', models.CharField(default='Indefinido', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status_Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Indefinido', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status_Uso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status_Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=1, max_length=50)),
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
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('rua', models.CharField(max_length=35)),
                ('bairro', models.CharField(max_length=35)),
                ('cidade', models.CharField(max_length=35)),
                ('cep', models.CharField(max_length=15)),
                ('imagem', models.ImageField(default='carro-escondido.jpg', upload_to='imagens/usuario')),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_permissions_set', to='auth.permission')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.estado')),
                ('status_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.statususuario')),
                ('tipo_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.tipousuario')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=100)),
                ('valor_compra', models.CharField(max_length=25)),
                ('ano', models.IntegerField()),
                ('km', models.CharField(max_length=20)),
                ('motor', models.CharField(max_length=10)),
                ('placa', models.CharField(max_length=20)),
                ('chassi', models.CharField(max_length=20)),
                ('cor', models.CharField(default='indefinido', max_length=50)),
                ('imagem', models.ImageField(default='media/carro-escondido.jpg', upload_to='imagens/veiculos')),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veiculos_status', to='dashboard.status_veiculo')),
                ('usuario_alteracao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veiculos_alterados', to=settings.AUTH_USER_MODEL)),
                ('usuario_cadastro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veiculos_cadastrados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('data_entrega', models.DateField()),
                ('idade_condutor', models.IntegerField()),
                ('valor', models.FloatField()),
                ('forma_pagamento', models.CharField(max_length=30)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas_como_motorista', to=settings.AUTH_USER_MODEL)),
                ('usuario_alteracao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservas_alteradas', to=settings.AUTH_USER_MODEL)),
                ('usuario_cadastro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservas_cadastradas', to=settings.AUTH_USER_MODEL)),
                ('status_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas_status', to='dashboard.status_reserva')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='dashboard.veiculo')),
            ],
        ),
    ]
