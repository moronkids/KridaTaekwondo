# Generated by Django 2.1 on 2019-01-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0039_postmodel_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='gambar',
            field=models.ImageField(default='/Volumes/Data/Basic-Django-2.1/mario/media/images/vespa.jpg', upload_to='images'),
        ),
    ]
