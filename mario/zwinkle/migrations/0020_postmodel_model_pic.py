# Generated by Django 2.1 on 2019-01-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0019_auto_20190112_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='model_pic',
            field=models.ImageField(default='static/pic_folder/none/taekwondo.jpg', upload_to='static/pic_folder/'),
        ),
    ]
