# Generated by Django 4.2.4 on 2023-08-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='no name...', max_length=120),
        ),
    ]
