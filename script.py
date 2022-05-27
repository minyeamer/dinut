import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dinut.settings")
django.setup()

from dietapp.models import Nutrition, Diet

NUTRITION_DB = 'script/nutrition.csv'
DIET_DB = 'script/diet.csv'

with open(NUTRITION_DB) as nutrition_csv:
    rows = csv.reader(nutrition_csv)
    next(rows, None)
    for row in rows:
        Nutrition.objects.create(
            food_name = row[1],
            product_name = row[2],
            main_cat = row[3],
            sub_cat = row[4],
            energy = row[5],
            carb = row[6],
            protein = row[7],
            fat = row[8],
            sugar = row[9],
            fiber = row[10],
            sodium = row[11],
        )

with open(DIET_DB) as diet_csv:
    rows = csv.reader(diet_csv)
    next(rows, None)
    for row in rows:
        Diet.objects.create(
            food_list = row[1],
            energy = row[2],
            carb = row[3],
            protein = row[4],
            fat = row[5],
            vitamin_a = row[6],
            riboflavin = row[7],
            calcium = row[8],
            iron = row[9],
        )
