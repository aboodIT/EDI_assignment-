from django.db import models

# Create your models here.

class team_model(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    # def employee(self):
    #     if not hasattr(self, '_employee'):
    #         self._employee = self.employee_set.all()
    #     return self._employee

class work_model(models.Model): 
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class employee_model(models.Model):
    team = models.ForeignKey(team_model,to_field='name',on_delete=models.CASCADE)
    name = models.CharField(max_length=50,unique=True)
    leader = models.BooleanField()
    pay = models.PositiveIntegerField()
    work_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class leaders_model(models.Model):
    name = models.ForeignKey(employee_model,to_field='name',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


