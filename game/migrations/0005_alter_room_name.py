# Generated by Django 5.2.1 on 2025-05-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.TextField(default='GameRoom'),
        ),
    ]
