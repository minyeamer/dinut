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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField('별명', max_length=20, null=False, unique=True)
    height = models.IntegerField('키(cm)', null=False, validators=[MinValueValidator(1)])
    weight = models.IntegerField('몸무게(kg)', null=False, validators=[MinValueValidator(1)])
    age = models.IntegerField('나이', null=False, validators=[MinValueValidator(0)])
    gender = models.CharField('성별', max_length=1, null=False, choices=GENDERS)
    activity = models.CharField('활동 및 운동 수준', max_length=255, null=False, choices=ACTIVITY)
    bmr = models.FloatField('기초대사량', null=False, validators=[MinValueValidator(0.0)])
    caloric_burn = models.FloatField('활동대사량', null=False, validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'profile'
        verbose_name_plural = '프로필'

    def fill_values(self, user: User):
        self.user = user
        self.bmr = self.calc_bmr()
        self.caloric_burn = self.calc_caloric_burn()
        self.save()

    def calc_bmr(self) -> float:
        # Mifflin-St. Jeor Caculator
        gender_weight = {'M':5,'F':-161}
        return round(10*self.weight + 6.25*self.height - 5*self.age + gender_weight[self.gender], 2)

    def calc_caloric_burn(self) -> float:
        # Mifflin-St. Jeor Caculator
        activity_level = {
            'sedentary':1.2,
            'slightly':1.375,
            'moderately':1.55,
            'very':1.725,
            'extra':1.9,
        }
        return round(self.bmr * activity_level[self.activity], 2)

    def __str__(self):
        return f'사용자 {self.pk}: {self.nickname}, 기초대사량: {self.bmr}, 활동대사량: {self.caloric_burn}'
