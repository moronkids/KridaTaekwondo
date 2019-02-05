# Generated by Django 2.1.4 on 2019-01-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0006_auto_20181230_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='penulis',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='isi',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='kategori',
            field=models.CharField(choices=[('ME', '1'), ('YOU', '2'), ('WE', '3')], default=1, max_length=100),
        ),
    ]