# Generated by Django 3.2.8 on 2023-02-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disqueria', '0005_alter_interprete_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='caratula',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Carátula'),
        ),
    ]
