from django.db import models

# Create your models here.

class Category(models.Model):
    name_category = models.CharField(verbose_name='название котегории',max_length=100)

    def __str__(self):
        return self.name_category
