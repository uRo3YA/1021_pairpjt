from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    img = models.TextField()


class Review(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    star_Choices = (
        ("⭐", "⭐"),
        ("⭐⭐", "⭐⭐"),
        ("⭐⭐⭐", "⭐⭐⭐"),
        ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
        ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
    )
    star = models.CharField(max_length=10, choices=star_Choices)
    description = RichTextUploadingField(blank=True, null=True)


class Comment(models.Model):
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
