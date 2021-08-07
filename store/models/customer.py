
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin =  models.IntegerField(default=0)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
           return Customer.objects.get(email= email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

