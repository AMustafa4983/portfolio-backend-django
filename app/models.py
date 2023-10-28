from django.db import models
from django_mysql.models import ListCharField
from django.conf import settings

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    hint = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.CharField(max_length=200)
    demo_link = models.CharField(max_length=200)
    skills = ListCharField(
        base_field = models.CharField(max_length=50),
        size=10,
        max_length=(10 *51)
        )
    image1 = models.FileField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, default='media/default.jpg')
    image2 = models.FileField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, default='media/default.jpg')
    image3 = models.FileField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, default='media/default.jpg')
    image4 = models.FileField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, default='media/default.jpg')

    def __str__(self):
        return f"Project: {self.title}"
    

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=200)

    def __str__(self):
        return f"Project: {self.title}"
    
class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    job_title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.CharField(max_length=80)

    def __str__(self):
        return f"Project: {self.title}"
    

class MyCV(models.Model):
    pdfFile = models.FileField(upload_to='resume')