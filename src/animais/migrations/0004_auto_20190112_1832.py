# Generated by Django 2.1.1 on 2019-01-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0003_auto_20190112_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bovino',
            name='peso',
            field=models.TextField(blank=True, null=True, verbose_name='Peso em Kg e sua Data'),
        ),
    ]
