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
    nickname = models.CharField(max_length=20, unique=True)
    height = models.PositiveIntegerField(verbose_name='키(cm)',validators=[MinValueValidator(1)])
    weight = models.PositiveIntegerField(verbose_name='몸무게(kg)',validators=[MinValueValidator(1)])
    age = models.PositiveIntegerField(verbose_name='나이')
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    activity = models.CharField(verbose_name='활동 및 운동 수준', max_length=255, choices=ACTIVITY)
    bmr = models.PositiveIntegerField(verbose_name='기초대사량')
    caloric_burn = models.PositiveIntegerField(verbose_name='활동대사량')

    def fill_secret_values(self, user: User):
        self.user = user
        self.calc_bmr()
        self.calc_caloric_burn()
        self.save()

    def calc_bmr(self):
        # Mifflin-St. Jeor Caculator
        gender_weight = {'M':5,'F':-161}
        self.bmr = int(10*self.weight + 6.25*self.height - 5*self.age + gender_weight[self.gender])

    def calc_caloric_burn(self):
        # Mifflin-St. Jeor Caculator
        activity_level = {
            'sedentary':1.2,
            'slightly':1.375,
            'moderately':1.55,
            'very':1.725,
            'extra':1.9,
        }
        self.caloric_burn = self.bmr * activity_level[self.activity]

    def __str__(self):
        return 'pk {}: {} - {}'.format(self.pk, self.nickname, self.caloric_burn)
