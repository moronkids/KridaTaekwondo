# Generated by Django 2.1 on 2019-01-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0038_auto_20190114_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(default='x', upload_to='images'),
        ),
    ]