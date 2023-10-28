from rest_framework import serializers
from .models import *

class ProjcetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'title', 'hint', 'description', 'github_link', 'demo_link', 'skills', 'image1', 'image2', 'image3', 'image4')


class EductaionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'title', 'major', 'description', 'date')

class ExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('id', 'title', 'job_title', 'description', 'date')

class MyCVSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyCV
        field = ('pdfFile')