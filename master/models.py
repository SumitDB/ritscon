from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = PhoneNumberField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name