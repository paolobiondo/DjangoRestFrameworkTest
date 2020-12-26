from django.db import models
from django.utils.timezone import now

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    date = models.DateField(default=now)

    def __str__(self):
        return self.title