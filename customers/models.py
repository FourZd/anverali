from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    experience = models.TextField()

    def __str__(self):
        return self.name