from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserProfile(AbstractUser):
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)


class Post(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField(null=True)

    def generate_filename(instance, filename):
        extension = filename.split('.')[-1]
        new_filename = f"{uuid.uuid4()}.{extension}"
        return f'post_images/{new_filename}'

    image = models.ImageField(upload_to=generate_filename, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="likes"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']
