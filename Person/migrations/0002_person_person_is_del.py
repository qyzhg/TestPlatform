# Generated by Django 3.0.6 on 2020-05-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_is_del',
            field=models.BooleanField(default=False),
        ),
    ]