# Generated by Django 5.1 on 2024-08-29 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_demonstracaoresultado_receita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demonstracaoresultado',
            name='receita',
        ),
    ]
