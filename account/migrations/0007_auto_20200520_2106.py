# Generated by Django 3.0.5 on 2020-05-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_userprofile_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='account/avatars/%Y/%m/%d/'),
        ),
    ]