# Generated by Django 4.0.4 on 2022-05-27 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4b3e7b98-e1dc-4b9d-9ca3-8963651165f7'), editable=False, primary_key=True, serialize=False),
        ),
    ]
