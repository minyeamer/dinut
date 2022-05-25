from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from dietapp.detect import detect_food


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

    def reset_nutritions(self):
        self.energy = 0.0
        self.carb = 0.0
        self.protein = 0.0
        self.fat = 0.0
        self.sugar = 0.0
        self.fiber = 0.0
        self.sodium = 0.0
        self.vitamin_a = 0.0
        self.riboflavin = 0.0
        self.calcium = 0.0
        self.iron = 0.0


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
    food_list = models.TextField('식품 목록')

    class Meta:
        db_table = 'diet'
        verbose_name_plural = '식단'

    def analyze_diet(self, image_url: str):
        detect_result = detect_food(image_url)
        self.food_list = ', '.join(detect_result)

        for food in detect_result:
            nutrition = Nutrition.objects.get(food_name=food)
            self.energy += nutrition.energy
            self.carb += nutrition.carb
            self.protein += nutrition.protein
            self.fat += nutrition.fat
            self.sugar += nutrition.sugar
            self.fiber += nutrition.fiber
            self.sodium += nutrition.sodium
            self.vitamin_a = nutrition.vitamin_a
            self.riboflavin = nutrition.riboflavin
            self.calcium = nutrition.calcium
            self.iron = nutrition.iron

    def __str__(self):
        return f'{self.food_list} - {self.energy} kcal'


class AbstractUpload(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upload')
    updated_date = models.DateTimeField('업데이트 날짜', auto_now=True, null=False)

    class Meta:
        abstract = True


class DietImage(Diet, AbstractUpload):
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='diet')
    upload_diet = models.ImageField('업로드 식단', upload_to='images/diet/%Y/%m/%d', null=False)

    class Meta:
        db_table = 'diet_image'
        verbose_name_plural = '식단 이미지'


class DailyDietImage(Diet, AbstractUpload):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily')
    morning_diet = models.ImageField('아침 식단', upload_to='images/daily/morning/%Y/%m/%d', null=True)
    lunch_diet = models.ImageField('점심 식단', upload_to='images/daily/lunch/%Y/%m/%d', null=True)
    dinner_diet = models.ImageField('저녁 식단', upload_to='images/daily/dinner/%Y/%m/%d', null=True)
    snack_diet = models.ImageField('간식 식단', upload_to='images/daily/snack/%Y/%m/%d', null=True)

    class Meta:
        db_table = 'daily_diet_image'
        verbose_name_plural = '하루 식단 이미지'

    def calc_nutritions(self):
        self.reset_nutritions()

        diet_list = [diet for diet in
            [self.morning_diet, self.lunch_diet, self.dinner_diet, self.snack_diet] if diet]

        for diet in diet_list:
            self.analyze_diet(diet.url)

    def __str__(self):
        return f'{self.user} - {self.energy} kcal'
