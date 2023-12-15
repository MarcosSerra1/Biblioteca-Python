# Generated by Django 4.2.7 on 2023-12-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyblioteca', '0002_alter_livros_capitulos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='lancado_em',
            new_name='data_de_lancamento',
        ),
        migrations.AlterField(
            model_name='livros',
            name='capitulos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_de_leitura',
            field=models.CharField(max_length=100),
        ),
    ]
