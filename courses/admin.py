from django.contrib import admin
from .models import (
    CourseCategory, ExerciseCategory, ExamCategory,
    Course, Comment, Document, Video,

)

# -------------------------
# CATEGORY ADMINS
# -------------------------
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(ExamCategory)
class ExamCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


# -------------------------
# COURSE ADMIN
# -------------------------

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'category', 'level', 'created_at']
    list_filter = ['category', 'level', 'created_at']
    search_fields = ['title', 'description', 'instructor']
    ordering = ['-created_at']
    list_per_page = 20
    readonly_fields = ['created_at']
    fields = [
        'title', 'description', 'content', 'instructor',
        'category', 'level',
        'image', 'video_url', 'pdf_file',
        'created_at'
    ]


# -------------------------
# COMMENT ADMIN
# -------------------------

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'created_at']
    search_fields = ['name', 'content']
    list_filter = ['created_at', 'course']
    ordering = ['-created_at']

    

# -------------------------
# OTHER MODELS
# -------------------------

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["title", "exercise_category", "exam_category", "level"]
    list_filter = ["exercise_category", "exam_category", "level"]
    search_fields = ["title"]

admin.site.register(Video)
