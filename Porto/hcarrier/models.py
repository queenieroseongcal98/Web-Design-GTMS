from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField()

    def __str__(self):
        return self.name +" - " + self.email


class Transactions(models.Model):
    address = models.CharField(max_length=50)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.address
    

class Payment(models.Model):
    confirmation = models.CharField(max_length=50)

    def __str__(self):
        return self.confirmation