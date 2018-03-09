from django.db import models

# Create your models here.

class students(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=10, null=True)
    age = models.IntegerField(default=0)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class students_detail(models.Model):
    id=models.AutoField
    student_id=models.IntegerField(default=0)
    mather_name=models.CharField(max_length=10,null=True)
    father_name=models.CharField(max_length=10,null=True)
    mather_age=models.IntegerField(default=0)
    father_age=models.IntegerField(default=0)