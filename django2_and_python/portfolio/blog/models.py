from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100, default="Blog title")
    pub_date = models.DateTimeField(name="Date published", default=timezone.now)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title
