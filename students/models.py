from django.db import models


# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100, unique=True, default='Name')
  address = models.CharField(max_length=2552, default='Address')
  city = models.CharField(max_length=100, default='City')
  country = models.CharField(max_length=100, default='country')
  pincode = models.CharField(max_length=20, default='00000')
  sat_score = models.IntegerField(default=00)
  
  
  def calculate_passed(self):
    return "Pass" if self.sat_score > 30 else "Fail"
      
  def __str__(self):
    return f'Student: {self.name}'
