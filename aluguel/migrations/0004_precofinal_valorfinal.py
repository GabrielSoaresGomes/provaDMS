# Generated by Django 3.2 on 2021-11-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0003_auto_20211104_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='precofinal',
            name='valorFinal',
            field=models.FloatField(default=0, verbose_name=''),
            preserve_default=False,
        ),
    ]