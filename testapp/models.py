from django.db import models

# Create your models here.
class resume(models.Model):
    choices=(
    ( 'male',"Male",),
    ('female',"Female"),
    ("other","Other"))
    name=models.CharField(max_length=30)
    Father_name=models.CharField(max_length=30)
    Mother_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10,choices=choices ,default='female')
    City=models.CharField(max_length=256)
    State=models.CharField(max_length=256)
    Email=models.EmailField(max_length=30)
    contact_no=models.IntegerField()
    # programming_languages=models.CharField(max_length=500)
class personal_info(models.Model):
   permanent_Address=models.CharField(max_length=256)
   DOB=models.DateField()
   Hobbies=models.CharField(max_length=256)
   Languages=models.CharField(max_length=256)
class career_info(models.Model):
   career_objective=models.TextField()

class exam_info(models.Model):
   examination=models.CharField(max_length=50)
   Board_university=models.CharField(max_length=100)
   Institute=models.CharField(max_length=100)
   Year_of_passing=models.IntegerField()
   cgpa_percentage=models.CharField(max_length=50)
