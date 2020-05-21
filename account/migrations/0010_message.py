# Generated by Django 3.0.5 on 2020-05-21 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200520_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_mes', to='account.UserProfile')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_mes', to='account.UserProfile')),
            ],
        ),
    ]