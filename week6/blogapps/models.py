from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000) # 제목
    contents = models.TextField() # 본문
    updated_at = models.DateTimeField(auto_now=True) #글 작성 시간

    def summary(self):
        return self.contents[:100]