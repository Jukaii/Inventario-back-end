# Generated by Django 4.0.6 on 2022-08-03 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_categoria_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='material',
            field=models.IntegerField(default=0),
        ),
    ]
