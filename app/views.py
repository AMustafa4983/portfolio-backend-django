from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
import base64

class ProjectView(APIView):
    def get(self, request, id):
        project = Project.objects.get(id=id)

        output = []

        images = [
            self.encode_image(project.image1),
            self.encode_image(project.image2),
            self.encode_image(project.image3),
            self.encode_image(project.image4)
        ]

        data = {
            "id": project.id,
            "title": project.title,
            "hint": project.hint,
            "description": project.description,
            "github_link": project.github_link,
            "demo_link": project.demo_link,
            "skills": project.skills,
            "images": images
        }

        output.append(data)

        return Response(output)
    
    def encode_image(self, image_field):
        if image_field:
            with open(image_field.path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                return f"data:image/{image_field.name.split('.')[-1]};base64,{encoded_image}"
        else:
            return None
    
class ProjectsView(APIView):
    def get(self, request):
        projects = Project.objects.all()

        output = []

        for project in projects:
            images = [
                self.encode_image(project.image1),
                self.encode_image(project.image2),
                self.encode_image(project.image3),
                self.encode_image(project.image4)
            ]

            data = {
                "id": project.id,
                "title": project.title,
                "hint": project.hint,
                "description": project.description,
                "github_link": project.github_link,
                "demo_link": project.demo_link,
                "skills": project.skills,
                "images": images
            }

            output.append(data)

        return Response(output)
    
    def post(self, request):
        serializer = ProjcetSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    def encode_image(self, image_field):
        if image_field:
            with open(image_field.path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                return f"data:image/{image_field.name.split('.')[-1]};base64,{encoded_image}"
        else:
            return None
        
class EducationView(APIView):
    def get(self, request):
        education = Education.objects.all()

        output = []

        for edu in education:
            
            data = {
                "id": edu.id,
                "title": edu.title,
                "major": edu.major,
                "description": edu.description,
                "date": edu.date,
            }

            output.append(data)

        return Response(output)
    
class ExperienceView(APIView):
    def get(self, request):
        experiences = Experience.objects.all()

        output = []

        for exp in experiences:
            
            data = {
                "id": exp.id,
                "title": exp.title,
                "job_title": exp.job_title,
                "description": exp.description,
                "date": exp.date,
            }

            output.append(data)

        return Response(output)
    
class MyCVView(APIView):
        
    def encode_pdf(self, pdf_field):
        if pdf_field:
            with open(pdf_field.path, "rb") as pdf_file:
                encoded_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
                return f"data:pdf/{pdf_field.name.split('.')[-1]};base64,{encoded_pdf}"
        else:
            return None
        
    def get(self, request):
        CV = MyCV.objects.last()

        pdf = self.encode_pdf(CV.pdfFile)
        response = Response(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="AbdelrahmanMohamed.pdf"'
        return response
    
