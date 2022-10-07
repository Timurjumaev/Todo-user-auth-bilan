from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    fullname=models.CharField(max_length=30)
    guruh=models.CharField(max_length=50, blank=True)
    st_raqam=models.CharField(max_length=50, blank=True)
    tel=models.CharField(max_length=50, blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self): return self.fullname

class Reja(models.Model):
    nom=models.CharField(max_length=20)
    sana=models.DateField()
    batafsil=models.TextField()
    holat=models.CharField(max_length=20)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    def __str__(self): return self.nom


