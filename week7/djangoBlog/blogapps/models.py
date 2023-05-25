from django.db import models
# foreign ket 활용하기 위해 User model 가져오기
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    playtime = models.IntegerField()
    review = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def summary(self):
        return self.review[:10]

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment
    