# Generated by Django 4.2.5 on 2023-10-28 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_project_image1_project_image2_project_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image4',
            field=models.FileField(default='media/default.jpg', upload_to='media'),
        ),
    ]