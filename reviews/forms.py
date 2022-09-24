from django import forms
from .models import Review, Comment, Movie
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "star",
            "description",
        ]
        labels = {"title": "제목", "description": "내용", "star": "평점"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "제목을 입력해주세요"}
            ),
            "description": forms.CharField(
                widget=CKEditorUploadingWidget(), label=False
            ),
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
