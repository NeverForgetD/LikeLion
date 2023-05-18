from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    playtime = models.FloatField()
    review = models.TextField()

    def summary(self):
        return self.review[:10]

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.comment
    