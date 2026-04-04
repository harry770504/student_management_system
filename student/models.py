from django.db import models
from django.contrib.auth.models import User
from teacher.models import Teacher

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50, default='B.tech')
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.full_name
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)
    subject_code = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.subject_name    


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    exam_type = models.CharField(max_length=50)   # Midterm, Final, Unit Test
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.subject_name} - {self.marks_obtained}"
# Create your models here.


