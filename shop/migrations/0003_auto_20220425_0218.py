# Generated by Django 2.1.5 on 2022-04-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220425_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner_name',
            field=models.CharField(max_length=50),
        ),
    ]
