from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)  
    city = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return  self.name
    
class Marks(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    math = models.IntegerField()
    english = models.IntegerField()
    gujarati = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    hindi = models.IntegerField()

    total = models.IntegerField()
    per = models.FloatField()

    def __str__(self):
        return self.student.name