from django.db import models

# Create your models here.
class AcadInfo(models.Model):
    uid = models.IntegerField(default=0)
    firstname = models.CharField(max_length=64, default='name')
    lastname = models.CharField(max_length=64, default='surname')
    university = models.IntegerField(default=1)
    ugmajor = models.CharField(max_length=64, default='major')
    gpa = models.IntegerField(default=4)
    greq = models.IntegerField(default=170)
    grev = models.IntegerField(default=170)
    greawa = models.IntegerField(default=4)
    lor1n = models.CharField(max_length=100, default='Chinmay Agrawal')
    lor1 = models.EmailField(default='chinmayagrawal90@gmail.com')
    lor2n = models.CharField(max_length=100, default='Chinmay Agrawal')
    lor2 = models.EmailField(default='chinmayagrawal90@gmail.com')
    lor3n = models.CharField(max_length=100, default='Chinmay Agrawal')
    lor3 = models.EmailField(default='chinmayagrawal90@gmail.com')
    wmonths = models.IntegerField(default=12)
    wtype = models.CharField(max_length=64, default='FAANG')
    rmonths = models.IntegerField(default=12)
    pubven = models.CharField(max_length=64, default='ICML')
    score = models.FloatField(default=0)

