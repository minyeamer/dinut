# Create your models here.
from django.db import models

class ImageUploadModel(models.Model):
    #uid = 
    #upload_date =  models.DateTimeField(auto_now = True)
    foodImage = models.ImageField(upload_to='images/%Y/%m/%d')
    #morning_food = 
    #afternoon_food = 
    #dinner_food =
    #dissert =
