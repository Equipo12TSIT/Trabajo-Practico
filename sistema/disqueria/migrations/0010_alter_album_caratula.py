# Generated by Django 3.2.8 on 2023-02-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disqueria', '0009_alter_album_caratula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='caratula',
            field=models.ImageField(default='imagenes/caratula.jpg', null=True, upload_to='imagenes/', verbose_name='Carátula'),
        ),
    ]
