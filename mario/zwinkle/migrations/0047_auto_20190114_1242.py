# Generated by Django 2.1 on 2019-01-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0046_auto_20190114_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
