# Generated by Django 4.2.3 on 2023-07-26 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_saida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saida',
            old_name='material',
            new_name='materiais',
        ),
    ]
