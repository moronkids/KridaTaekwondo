# Generated by Django 2.1 on 2018-11-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zwinkle', '0003_auto_20181106_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='buat_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='konten',
            name='isi',
            field=models.TextField(),
        ),
    ]
