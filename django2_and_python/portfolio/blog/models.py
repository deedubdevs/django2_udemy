from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100, default="Blog title")
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title + ', ' + self.pub_date_pretty()

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
