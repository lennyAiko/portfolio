from django.db import models

# Create your models here.
 
class Projects(models.Model):
     """A class to contain all projects built"""
     name = models.CharField(max_length=150)
     framework = models.CharField(max_length=40)
     desc = models.CharField(max_length=250)
     date_added = models.DateField(auto_now_add=True)

     class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

     def __str__(self):
         return self.name

