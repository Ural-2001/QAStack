# Generated by Django 3.0.5 on 2020-05-16 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qa.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='qa.Theme'),
            preserve_default=False,
        ),
    ]