# Generated by Django 5.1.3 on 2025-02-24 00:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status_Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=1, max_length=50)),
                ('status_cor', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=100)),
                ('valor_compra', models.FloatField()),
                ('ano', models.IntegerField()),
                ('km', models.IntegerField()),
                ('motor', models.CharField(max_length=10)),
                ('placa', models.CharField(max_length=20)),
                ('chassi', models.CharField(max_length=20)),
                ('cor', models.CharField(default='indefinido', max_length=50)),
                ('imagem', models.ImageField(default='media/carro-escondido.jpg', upload_to='imagens/veiculos')),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veiculos_status', to='veiculos.status_veiculo')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veiculos.tipo_veiculo')),
                ('usuario_alteracao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veiculos_alterados', to=settings.AUTH_USER_MODEL)),
                ('usuario_cadastro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='veiculos_cadastrados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
