# Generated by Django 3.2 on 2022-05-28 14:39

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
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='에너지(kcal)')),
                ('carb', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='탄수화물(g)')),
                ('protein', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='단백질(g)')),
                ('fat', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='지방(g)')),
                ('sugar', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='당류(g)')),
                ('fiber', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='식이섬유(g)')),
                ('sodium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='나트륨(mg)')),
                ('vitamin_a', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='비타민A(R.E)')),
                ('riboflavin', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='리보플라빈(mg)')),
                ('calcium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='칼슘(mg)')),
                ('iron', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='철분(mg)')),
                ('diet_name', models.CharField(max_length=255, unique=True, verbose_name='식단명')),
                ('food_list', models.TextField(verbose_name='식품 목록')),
            ],
            options={
                'verbose_name_plural': '식단',
                'db_table': 'diet',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='에너지(kcal)')),
                ('carb', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='탄수화물(g)')),
                ('protein', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='단백질(g)')),
                ('fat', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='지방(g)')),
                ('sugar', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='당류(g)')),
                ('fiber', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='식이섬유(g)')),
                ('sodium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='나트륨(mg)')),
                ('vitamin_a', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='비타민A(R.E)')),
                ('riboflavin', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='리보플라빈(mg)')),
                ('calcium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='칼슘(mg)')),
                ('iron', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='철분(mg)')),
                ('food_name', models.CharField(max_length=255, unique=True, verbose_name='식품명')),
                ('product_name', models.CharField(max_length=255, verbose_name='상품명')),
                ('main_cat', models.CharField(max_length=255, verbose_name='식품 대분류')),
                ('sub_cat', models.CharField(max_length=255, verbose_name='식품 상세분류')),
            ],
            options={
                'verbose_name_plural': '영양정보',
                'db_table': 'nutrition',
            },
        ),
        migrations.CreateModel(
            name='DietImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='에너지(kcal)')),
                ('carb', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='탄수화물(g)')),
                ('protein', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='단백질(g)')),
                ('fat', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='지방(g)')),
                ('sugar', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='당류(g)')),
                ('fiber', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='식이섬유(g)')),
                ('sodium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='나트륨(mg)')),
                ('vitamin_a', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='비타민A(R.E)')),
                ('riboflavin', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='리보플라빈(mg)')),
                ('calcium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='칼슘(mg)')),
                ('iron', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='철분(mg)')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
                ('upload_diet', models.ImageField(upload_to='images/diet/%Y/%m/%d', verbose_name='업로드 식단')),
                ('food_list', models.TextField(verbose_name='식품 목록')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diet_image', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '식단 이미지',
                'db_table': 'diet_image',
            },
        ),
        migrations.CreateModel(
            name='DailyDietImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='에너지(kcal)')),
                ('carb', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='탄수화물(g)')),
                ('protein', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='단백질(g)')),
                ('fat', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='지방(g)')),
                ('sugar', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='당류(g)')),
                ('fiber', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='식이섬유(g)')),
                ('sodium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='나트륨(mg)')),
                ('vitamin_a', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='비타민A(R.E)')),
                ('riboflavin', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='리보플라빈(mg)')),
                ('calcium', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='칼슘(mg)')),
                ('iron', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='철분(mg)')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='업데이트 날짜')),
                ('morning_diet', models.ImageField(null=True, upload_to='images/daily/morning/%Y/%m/%d', verbose_name='아침 식단')),
                ('lunch_diet', models.ImageField(null=True, upload_to='images/daily/lunch/%Y/%m/%d', verbose_name='점심 식단')),
                ('dinner_diet', models.ImageField(null=True, upload_to='images/daily/dinner/%Y/%m/%d', verbose_name='저녁 식단')),
                ('snack_diet', models.ImageField(null=True, upload_to='images/daily/snack/%Y/%m/%d', verbose_name='간식 식단')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_diet_image', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '하루 식단 이미지',
                'db_table': 'daily_diet_image',
            },
        ),
    ]
