from django.db import models

# Create your models here.

class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=100)
    def __str__(self):
        return self.coursename



class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete= models.CASCADE)
    sp = models.CharField(max_length=200)
    il = models.CharField(max_length=200)
    def _str_(self):
        return self.sp

        

