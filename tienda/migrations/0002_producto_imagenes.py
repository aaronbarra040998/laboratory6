# Generated by Django 3.2 on 2023-04-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to='producto_imagenes/'),
        ),
    ]
