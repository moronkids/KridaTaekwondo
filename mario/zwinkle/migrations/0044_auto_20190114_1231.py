# Generated by Django 2.1 on 2019-01-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0043_auto_20190114_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.FileField(upload_to='images'),
        ),
    ]