from django.db import models

# Create your models here.

class team_model(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class work_model(models.Model): 
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class employee_model(models.Model):
    name = models.CharField(max_length=50,unique=True)
    leader = models.BooleanField()
    team = models.ForeignKey(Team_model,on_delete=models.CASCADE)
    arrangment = models.ForeignKey(work_model,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class leaders_model(models.Model):
    name = models.ForeignKey(Employee_model,to_field='name',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


