# Generated by Django 4.0.5 on 2022-07-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_message_recipient_alter_message_sender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]