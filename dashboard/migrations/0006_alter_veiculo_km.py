# Generated by Django 5.1.3 on 2025-02-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_status_manutencao_status_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='km',
            field=models.IntegerField(),
        ),
    ]
