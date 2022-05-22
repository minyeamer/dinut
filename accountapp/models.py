from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

GENDERS = (
    ('M', '남성'),
    ('W', '여성'),
)

ACTIVITY = (
    ('sedentary', '거의 운동 하지 않음음'),
    ('slightly', '가벼운 활동(주 1~3회)'),
    ('moderately', '보통 수준(주 3~5회)'),
    ('very', '적극적으로 운동(주 6~7회)'),
    ('extra', '매우 적극적으로 운동(주 6~7회)'),
)


# profileapp을 만들고 사용자 세부 정보를 해당 앱의 모델로 분리해야 합니다!
class CustomUser(User):
    height = models.PositiveIntegerField(verbose_name='키(cm)',validators=[MinValueValidator(1)])
    weight = models.PositiveIntegerField(verbose_name='몸무게(kg)',validators=[MinValueValidator(1)])
    age = models.PositiveIntegerField(verbose_name='나이')
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    activity = models.CharField(verbose_name='활동 및 운동 수준', max_length=255, choices=ACTIVITY)
    bmr = models.PositiveIntegerField(verbose_name='기초대사량')
    caloric_burn = models.PositiveIntegerField(verbose_name='활동대사량')
