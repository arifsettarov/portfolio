#!C:/Users/arif/AppData/Local/Programs/Python/Python35-32/python.exe
from django.db import models

# Create your models here.
class projects(models.Model):
    class Meta:
        db_table="projects"
    def __str__(self):
            return self.project_title
    project_title=models.CharField(max_length=50, verbose_name="Название")
    project_description=models.TextField(verbose_name="Описание")
    project_image=models.ImageField(verbose_name="Изображение (500х500)")
    project_url=models.URLField(verbose_name="GitHub URL")