from django.db import models

# Create your models here.
class Doctor(models.Model):
    Doctor_id=models.CharField(max_length=20)
    Doctor_name=models.CharField(max_length=100)
    Doctor_email=models.EmailField()
    Doctor_contact=models.CharField(max_length=20)

    def __str__(self):
        return self.Doctor_name
