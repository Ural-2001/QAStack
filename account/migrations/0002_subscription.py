# Generated by Django 3.0.5 on 2020-05-17 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='account.UserProfile')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='account.UserProfile')),
            ],
        ),
    ]