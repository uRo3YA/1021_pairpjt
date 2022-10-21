from django import forms
from .models import Review, Movie
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "description",
            "star",
        ]
        labels = {"title": "제목", "content": "내용", "description": "설명"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "제목을 입력해주세요"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "내용을 입력해주세요"}
            ),
            "description": forms.CharField(widget=CKEditorUploadingWidget()),
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
