# Generated by Django 5.0.6 on 2024-05-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
