from django.db import models
from django.utils import timezone

# Create your models here.
class New_coach(models.Model):
    coach_id = models.CharField(max_length=100,unique=True,primary_key=True)
    coach_category = models.CharField(max_length=100,blank=True,null=True)
    coach_name = models.CharField(max_length=100)
    coach_mail = models.EmailField(max_length=100,unique=True)
    date = models.DateTimeField(default=timezone.now)
    coach_url = models.FileField(upload_to='media/')
    coach_min_cost = models.IntegerField(default=0)
    coach_max_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.coach_id





