# Generated by Django 4.2.3 on 2023-07-26 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_revenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estoque.materiais')),
                ('revenda', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='estoque.revenda')),
            ],
        ),
    ]