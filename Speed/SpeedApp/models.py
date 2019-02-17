from django.db import models
class Article(models.Model):
    title =  models.CharField(max_length=20,verbose_name="Заголовок")
    text = models.TextField(max_length=20,verbose_name = "Xiaomi Mi 8 Lite")
    def __str__(self):
        return self.title

# Create your models here.
