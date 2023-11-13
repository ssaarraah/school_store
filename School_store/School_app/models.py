from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.
# class department(models.Model):
#     departmentname=models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.departmentname
#
# class Courses(models.Model):
#     dept_no = models.ForeignKey(department,on_delete=CASCADE)
#     course1 = models.CharField(max_length=50)
#     course2 = models.CharField(max_length=50)
#     course3 = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.course1





class School(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.BooleanField(null=True,blank=True)
    phone = models.IntegerField(max_length=10,null=True,blank=True)
    emailid = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=150,null=True,blank=True)
    dept = models.CharField(max_length=50,null=True,blank=True)
    courses1 = models.CharField(max_length=50,null=True,blank=True)
    purpose=models.CharField(max_length=50,null=True,blank=True)
    materials=models.CharField(max_length=50,null=True,blank=True)






    def __str__(self):
        return self.name


