# Generated by Django 3.2 on 2021-11-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precofinal',
            name='data',
            field=models.CharField(max_length=10, verbose_name='Insira a data no formato MM/DD/YYYY : '),
        ),
    ]
