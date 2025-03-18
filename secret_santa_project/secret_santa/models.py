from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class SecretSantaAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='giver')
    secret_child = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver')
    year = models.IntegerField()

    class Meta:
        unique_together = ('employee', 'year')

    def __str__(self):
        return f"{self.employee.name} -> {self.secret_child.name} ({self.year})"
