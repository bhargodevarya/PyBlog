from django.db import models
from django.db import models
# Create your models here.


class Blog(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    published_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} has content {self.content} and has been written by {self.author}'

class Comment(models.Model):
    user = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.content} was made by {self.user}'