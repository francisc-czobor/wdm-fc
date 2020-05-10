from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    class Meta:
        unique_together = ('author', 'title')

    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.lower().replace(' ', '-')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-details', args=[self.slug])

    def __str__(self):
        return self.title
