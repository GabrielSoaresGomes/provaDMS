# Generated by Django 3.2 on 2021-11-03 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0007_auto_20211103_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precofinal',
            old_name='estadioEscolhido',
            new_name='idEscolhido',
        ),
    ]
