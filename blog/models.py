from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200 )
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Texto do Blog")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{} - {}'.format(self.title, self.author)