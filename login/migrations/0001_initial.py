# Generated by Django 2.1.4 on 2019-07-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('user', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
