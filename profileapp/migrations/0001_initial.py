# Generated by Django 3.2 on 2022-05-23 07:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('height', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='키(cm)')),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='몸무게(kg)')),
                ('age', models.PositiveIntegerField(verbose_name='나이')),
                ('gender', models.CharField(choices=[('M', '남성'), ('W', '여성')], max_length=1, verbose_name='성별')),
                ('activity', models.CharField(choices=[('sedentary', '거의 운동 하지 않음음'), ('slightly', '가벼운 활동(주 1~3회)'), ('moderately', '보통 수준(주 3~5회)'), ('very', '적극적으로 운동(주 6~7회)'), ('extra', '매우 적극적으로 운동(주 6~7회)')], max_length=255, verbose_name='활동 및 운동 수준')),
                ('bmr', models.PositiveIntegerField(verbose_name='기초대사량')),
                ('caloric_burn', models.PositiveIntegerField(verbose_name='활동대사량')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
