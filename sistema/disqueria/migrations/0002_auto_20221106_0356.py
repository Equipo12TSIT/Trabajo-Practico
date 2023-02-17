# Generated by Django 3.2.8 on 2022-11-06 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disqueria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cant_temas',
            field=models.IntegerField(verbose_name='Cantidad de temas'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cantidad',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='album',
            name='caratula',
            field=models.FileField(null=True, upload_to='imagenes/', verbose_name='Carátula'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cod_album',
            field=models.IntegerField(verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='album',
            name='fec_lanzamiento',
            field=models.DateField(verbose_name='Lanzamiento'),
        ),
        migrations.AlterField(
            model_name='album',
            name='id_discografica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disqueria.discografica', verbose_name='Discográfica'),
        ),
        migrations.AlterField(
            model_name='album',
            name='id_formato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disqueria.formato', verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='album',
            name='id_genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disqueria.genero', verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='album',
            name='id_interprete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disqueria.interprete', verbose_name='Intérprete'),
        ),
        migrations.AlterField(
            model_name='album',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio'),
        ),
    ]