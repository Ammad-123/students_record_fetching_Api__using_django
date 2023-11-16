from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Model Object - Single Student Data
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)
    

# Query Set - All Student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu ,many=True)
    return JsonResponse(serializer.data,safe=False)

