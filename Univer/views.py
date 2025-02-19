from django.shortcuts import render
from .models import Kurs, Student  # Modelni import qilamiz


def salon(request):
    courses = Kurs.objects.all()  # Barcha kurslarni olish
    students = Student.objects.all()  # Barcha talabalarni olish

    return render(request, 'news/salon.html', {'courses': courses, 'students': students})
