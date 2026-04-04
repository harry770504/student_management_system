from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.models import Student, Subject, Marks
from teacher.models import Teacher
@login_required
def add_marks(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        exam_type = request.POST.get('exam_type')
        marks_obtained = request.POST.get('marks_obtained')
        total_marks = request.POST.get('total_marks')

        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)
        teacher = Teacher.objects.get(user=request.user)

        Marks.objects.create(
            student=student,
            subject=subject,
            teacher=teacher,
            exam_type=exam_type,
            marks_obtained=marks_obtained,
            total_marks=total_marks
        )

        return render(request, 'teachet/mark_numbers.html', {
            'students': students,
            'subjects': subjects,
            'success': 'Marks added successfully!'
        })

    return render(request, 'teacher/mark_numbers.html', {
        'students': students,
        'subjects': subjects
    })