# Generated by Django 4.1 on 2022-09-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('user_name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
            ],
        ),
    ]
