from django.db import models
from django.utils import timezone

from .post import Post


class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.deletion.CASCADE, related_name='comments')

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ''.join([
            self.author,
            ' - ',
            self.post,
        ])
