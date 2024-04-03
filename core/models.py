from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
