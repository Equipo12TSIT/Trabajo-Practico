# Generated by Django 3.2.8 on 2023-02-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disqueria', '0004_alter_album_caratula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interprete',
            name='foto',
            field=models.ImageField(default='imagenes/user.jpg', null=True, upload_to='imagenes/', verbose_name='foto'),
        ),
    ]