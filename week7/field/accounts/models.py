from django.db import models
# foreign ket 활용하기 위해 User model 가져오기
from django.contrib.auth.models import User

# Create your models here.

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title