from django.db import models

# Create your models here.
class Employee_model(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    pay = models.IntegerField()
    #leader = models.BooleanField()



    def __str__(self):
        return self.name