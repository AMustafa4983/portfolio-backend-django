# Generated by Django 4.2.5 on 2023-10-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_project_image1_alter_project_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=80)),
            ],
        ),
    ]
