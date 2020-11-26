from django.db import models
from django.utils import timezone

# Create your models here.
class New_cust(models.Model):
    cust_id = models.CharField(max_length=100,unique=True,primary_key=True)
    cust_name = models.CharField(max_length=100,null=True)
    cust_mail = models.EmailField(max_length=100,unique=True)
    cust_phone = models.CharField(max_length=100,unique=True)
    cust_pswd = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=timezone.now)
    cust_url = models.FileField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.cust_id





