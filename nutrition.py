import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dinut.settings")
django.setup()

from foodapp.models import Nutrition

CSV_PATH_PRODUCTS='script/nutrition.csv'

with open(CSV_PATH_PRODUCTS) as nutrition_csv:
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
