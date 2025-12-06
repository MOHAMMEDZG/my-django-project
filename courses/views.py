from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import (
    Course, CourseCategory, ExamCategory, ExerciseCategory, Video, Document
)
from .forms import CommentForm
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from .forms import InstructorCourseForm


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:4]
    comments = course.comments.all().order_by('-created_at')
    videos = Video.objects.filter(course=course)

    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.course = course
        comment.save()
        return redirect('course_detail', course_id=course.id)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'related_courses': related_courses,
        'comments': comments,
        'form': form,
        'videos': videos,
    })

def course_level(request, level):

    query = request.GET.get("q", "")
    category = request.GET.get("category", "all")

    # get courses level
    courses = Course.objects.filter(level=level)

    # search
    if query:
        courses = courses.filter(title__icontains=query)

    #  filter gategory
    if category != "all":
        courses = courses.filter(category_id=category)

    #  all categorys
    categories = CourseCategory.objects.all()

    LEVEL_DISPLAY = {
        "1": "الأولى إعدادي",
        "2": "الثانية إعدادي",
        "3": "الثالثة إعدادي",
    }

    level_name = LEVEL_DISPLAY.get(level, "غير معروف")

    return render(request, "courses/course_level.html", {
        "courses": courses,
        "categories": categories,
        "query": query,
        "level_name": level_name,
        "selected_category": category,
    })

def exercises_list(request):
    selected_category = request.GET.get("category")

    categories = ExerciseCategory.objects.all()

    if selected_category:
        docs = Document.objects.filter(exercise_category_id=selected_category)
    else:
        docs = Document.objects.filter(exercise_category__isnull=False)

    return render(request, "courses/exercises_list.html", {
        "docs": docs,
        "categories": categories,
        "selected_category": selected_category,
    })



def regional_exams(request):
    selected_category = request.GET.get("category")

    categories = ExamCategory.objects.all()

    if selected_category:
        docs = Document.objects.filter(exam_category_id=selected_category)
    else:
        docs = Document.objects.filter(exam_category__isnull=False)

    return render(request, "courses/regional_exams.html", {
        "docs": docs,
        "categories": categories,
        "selected_category": selected_category,
    })


def home(request):
    return render(request, 'courses/home.html')

def about(request):
    return render(request, 'courses/about.html')


def contact(request):
    return render(request, 'courses/contact.html')

@login_required
def instructor_add_course(request):
    if request.method == 'POST':
        form = InstructorCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user.username
            course.save()
            return redirect('instructor_dashboard')  
    else:
        form = InstructorCourseForm()

    return render(request, 'courses/instructor_add_course.html', {'form': form})
