# Generated by Django 4.2.5 on 2023-10-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_education_date_alter_experience_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfFile', models.FileField(upload_to='resume')),
            ],
        ),
    ]
