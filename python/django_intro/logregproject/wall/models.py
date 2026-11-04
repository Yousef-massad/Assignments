from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(
        "users.User",
        related_name="messages",
        on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        related_name="comments",
        on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        Message,
        related_name="comments",
        on_delete=models.CASCADE
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)