from django.db import models
from django.contrib.auth.models import User


class FoodImage(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='food')
    food_image = models.ImageField('이미지 주소', upload_to='images/%Y/%m/%d', null=False)
    upload_date =  models.DateTimeField('업로드 날짜', auto_now=True, null=False)


class Nutrition(models.Model):
    food_name = models.CharField('식품명', max_length=255, unique=True)
    product_name = models.CharField('상품명', max_length=255)
    main_cat = models.CharField('식품대분류', max_length=255)
    sub_cat = models.CharField('식품상세분류', max_length=255)
    energy = models.FloatField('에너지(kcal)', default=0)
    carb = models.FloatField('탄수화물(g)', default=0)
    protein = models.FloatField('단백질(g)', default=0)
    fat = models.FloatField('지방(g)', default=0)
    sugar = models.FloatField('당류(g)', default=0)
    fiber = models.FloatField('식이섬유(g)', default=0)
    sodium = models.FloatField('나트륨(mg)', default=0)

    def __str__(self):
        return f'{self.food_name} - {self.energy} kcal'
