# Generated by Django 4.0.5 on 2022-07-11 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receipient',
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='users.profile'),
        ),
    ]
