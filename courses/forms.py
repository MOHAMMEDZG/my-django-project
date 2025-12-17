from django import forms
from .models import Comment, Course

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your name',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'category',
            'image',
            'pdf_file',
            'video_url',
            'level',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.youtube.com/watch?v=xxxx'
            }),
        }

class InstructorCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'content',
            'category',
            'image',
            'pdf_file',
            'video_url',
            'level',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://youtu.be/xxxx'
            }),
        }
