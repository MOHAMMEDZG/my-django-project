from django.db import models
from django.contrib.auth.models import User


# ============================
# 1) COURSE CATEGORIES
# ============================
class CourseCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="صنف الدروس")

    class Meta:
        verbose_name="صنف الدرس"
        verbose_name_plural="صنف الدرس"


    def __str__(self):
        return self.name


# ============================
# 2) EXERCISE CATEGORIES
# ============================
class ExerciseCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="صنف التمارين")

    class Meta:
        verbose_name="صنف التمرين"
        verbose_name_plural="اصناف التمارين"


    def __str__(self):
        return self.name


# ============================
# 3) EXAM CATEGORIES
# ============================
class ExamCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="صنف الامتحانات")

    class Meta:
        verbose_name="صنف الامتحان"
        verbose_name_plural="اصناف الامتحانات"


    def __str__(self):
        return self.name


# ============================
# DOCUMENT MODEL (EXAMS)
# ============================
class Document(models.Model):
    title = models.CharField(max_length=200,verbose_name='العنوان' )
    file = models.FileField(upload_to="documents/", verbose_name='الملف')

    exercise_category = models.ForeignKey(
        ExerciseCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="exercise_docs", verbose_name='صنف التمرين'
    )

    exam_category = models.ForeignKey(
        ExamCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="exam_docs", verbose_name='صنف الامتحان'
    )

    level = models.CharField(max_length=20, null=True, blank=True, verbose_name='المستوى')

    class Meta:
        verbose_name="ملف pdf"
        verbose_name_plural="ملفات pdf"


    def __str__(self):
        return self.title



# ============================
# COURSE MODEL
# ============================
class Course(models.Model):
    LEVEL_CHOICES = [
        ('1', 'الأولى إعدادي'),
        ('2', 'الثانية إعدادي'),
        ('3', 'الثالثة إعدادي'),
    ]

    title = models.CharField(max_length=200, verbose_name='العنوان')
    description = models.TextField(verbose_name='الوصف')
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES,verbose_name='المستوى')
    content = models.TextField(blank=True, null=True, verbose_name='مضمون الدرس')
    instructor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='كتب بتاريخ')
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='الفئة')
    image = models.ImageField(upload_to='course_images/', blank=True, null=True, verbose_name='الصورة')
    video = models.FileField(upload_to='course_videos/', blank=True, null=True, verbose_name='الفيديو')
    video_url = models.URLField(blank=True, null=True, verbose_name='رابط الفيديو')
    pdf_file = models.FileField(upload_to='course_pdfs/', blank=True, null=True, verbose_name='ملف pdf')

    class Meta:
        verbose_name="الدرس"
        verbose_name_plural="الدروس"


    def __str__(self):
        return self.title


# ============================
# COMMENTS
# ============================
class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments',verbose_name='الدرس')
    name = models.CharField(max_length=100, verbose_name='الاسم')
    content = models.TextField(verbose_name='المحتوى')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='كتب بتاريخ')

    class Meta:
        verbose_name="التعليق"
        verbose_name_plural="التعليقات"


    def __str__(self):
        return f"{self.name} — {self.course.title}"


# ============================
# VIDEOS
# ============================
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos', verbose_name='الدرس')
    title = models.CharField(max_length=200, verbose_name='العنوان')
    youtube_url = models.URLField(verbose_name='رابط الفيديو')

    class Meta:
        verbose_name="الفيديو"
        verbose_name_plural="الفيديوهات"


    def get_embed_url(self):
        if "watch?v=" in self.youtube_url:
            return self.youtube_url.replace("watch?v=", "embed/")
        return self.youtube_url

    def __str__(self):
        return"{self.title} - {self.course.title}"
