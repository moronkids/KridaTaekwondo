# Generated by Django 2.1 on 2019-01-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0027_auto_20190113_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]