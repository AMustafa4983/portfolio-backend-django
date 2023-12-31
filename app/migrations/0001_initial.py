# Generated by Django 4.2.6 on 2023-10-27 23:51

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('hint', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('github_link', models.CharField(max_length=200)),
                ('demo_link', models.CharField(max_length=200)),
                ('skills', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=510, size=10)),
            ],
        ),
    ]
