# Generated by Django 2.1 on 2019-01-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0011_auto_20190110_0446'),
    ]

    operations = [
        migrations.DeleteModel(
            name='copy_krida_model',
        ),
        migrations.AlterField(
            model_name='krida_model',
            name='nama',
            field=models.CharField(max_length=30),
        ),
    ]