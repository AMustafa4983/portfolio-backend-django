# Generated by Django 4.2.5 on 2023-10-28 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_project_image1_alter_project_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image4',
        ),
    ]