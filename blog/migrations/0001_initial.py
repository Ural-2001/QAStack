# Generated by Django 3.0.5 on 2020-05-14 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='account.UserProfile')),
                ('users_likes', models.ManyToManyField(blank=True, related_name='posts_liked', to='account.UserProfile')),
            ],
        ),
    ]
