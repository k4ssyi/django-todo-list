from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_date = models.DateTimeField(
      blank=True, null=True
    )

    def publish(self):
        self.publish_date = timezone.now()
        self.save

    def __str__(self):
        return self.title

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)
