from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    posts = models.TextField()

    def __str__(self):
        return self.title

