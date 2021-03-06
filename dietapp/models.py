from typing import Dict
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class AbstractNutrition(models.Model):
    energy = models.FloatField('에너지(kcal)', default=0.0, validators=[MinValueValidator(0.0)])
    carb = models.FloatField('탄수화물(g)', default=0.0, validators=[MinValueValidator(0.0)])
    protein = models.FloatField('단백질(g)', default=0.0, validators=[MinValueValidator(0.0)])
    fat = models.FloatField('지방(g)', default=0.0, validators=[MinValueValidator(0.0)])
    sugar = models.FloatField('당류(g)', default=0.0, validators=[MinValueValidator(0.0)])
    fiber = models.FloatField('식이섬유(g)', default=0.0, validators=[MinValueValidator(0.0)])
    sodium = models.FloatField('나트륨(mg)', default=0.0, validators=[MinValueValidator(0.0)])
    vitamin_a = models.FloatField('비타민A(R.E)', default=0.0, validators=[MinValueValidator(0.0)])
    riboflavin = models.FloatField('리보플라빈(mg)', default=0.0, validators=[MinValueValidator(0.0)])
    calcium = models.FloatField('칼슘(mg)', default=0.0, validators=[MinValueValidator(0.0)])
    iron = models.FloatField('철분(mg)', default=0.0, validators=[MinValueValidator(0.0)])

    class Meta:
        abstract = True

    def fill_nutritions(self, nutrition_info: Dict[str, float]):
        self.energy = round(nutrition_info['energy'],2)
        self.carb = round(nutrition_info['carb'],2)
        self.protein = round(nutrition_info['protein'],2)
        self.fat = round(nutrition_info['fat'],2)
        self.sugar = round(nutrition_info['sugar'],2)
        self.fiber = round(nutrition_info['fiber'],2)
        self.sodium = round(nutrition_info['sodium'],2)
        self.vitamin_a = round(nutrition_info['vitamin_a'],2)
        self.riboflavin = round(nutrition_info['riboflavin'],2)
        self.calcium = round(nutrition_info['calcium'],2)
        self.iron = round(nutrition_info['iron'],2)


class AbstractUpload(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upload')
    updated_date = models.DateTimeField('업데이트 날짜', auto_now=True, null=False)

    class Meta:
        abstract = True


class Nutrition(AbstractNutrition):
    food_name = models.CharField('식품명', max_length=255, unique=True)
    product_name = models.CharField('상품명', max_length=255)
    main_cat = models.CharField('식품 대분류', max_length=255)
    sub_cat = models.CharField('식품 상세분류', max_length=255)

    class Meta:
        db_table = 'nutrition'
        verbose_name_plural = '영양정보'

    def __str__(self):
        return f'{self.food_name} - {self.energy} kcal'


class Diet(AbstractNutrition):
    diet_name = models.CharField('식단명', max_length=255, unique=True)
    food_list = models.TextField('식품 목록')

    class Meta:
        db_table = 'diet'
        verbose_name_plural = '식단'

    def __str__(self):
        return f'{self.diet_name} ({self.food_list}) - {self.energy} kcal'


class DietImage(AbstractNutrition, AbstractUpload):
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='diet_image')
    upload_diet = models.ImageField('업로드 식단', upload_to='images/diet/%Y/%m/%d', null=False)
    food_list = models.TextField('식품 목록')

    class Meta:
        db_table = 'diet_image'
        verbose_name_plural = '식단 이미지'

    def fill_values(self, uploader: User):
        if uploader.is_authenticated:
            self.uploader = uploader

        from dietapp.query import analyze_diet
        detect_result = analyze_diet(self.upload_diet.url)
        self.food_list = detect_result['food_list']
        self.fill_nutritions(detect_result)
        self.save()

    def __str__(self):
        return f'{self.food_list} - {self.energy} kcal'


class DailyDietImage(AbstractNutrition, AbstractUpload):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_diet_image')
    morning_diet = models.ImageField('아침 식단', upload_to='images/daily/morning/%Y/%m/%d', null=True, blank=True) 
    lunch_diet = models.ImageField('점심 식단', upload_to='images/daily/lunch/%Y/%m/%d', null=True, blank=True)
    dinner_diet = models.ImageField('저녁 식단', upload_to='images/daily/dinner/%Y/%m/%d', null=True, blank=True)
    snack_diet = models.ImageField('간식 식단', upload_to='images/daily/snack/%Y/%m/%d', null=True, blank=True)
    target_date = models.DateField('일자', auto_now=False, null=True) 

    class Meta:
        db_table = 'daily_diet_image'
        verbose_name_plural = '하루 식단 이미지'

    def fill_values(self, uploader: User):
        self.uploader = uploader
        upload_diet_list = [upload_diet.url for upload_diet in
            [self.morning_diet, self.lunch_diet, self.dinner_diet, self.snack_diet] if upload_diet]

        from dietapp.query import sum_nutritions
        calc_result = sum_nutritions(upload_diet_list)
        self.fill_nutritions(calc_result)
        self.save()

    def __str__(self):
        return f'{self.uploader} - {self.energy} kcal'
