import os
import sys
import django
import csv


def execute_nutrition_db():
    from dietapp.models import Nutrition
    from django.conf import settings
    NUTRITION_DB = os.path.join(settings.DB_DIR, 'nutrition.csv')

    with open(NUTRITION_DB, 'r', encoding='UTF-8') as nutrition_csv:
        rows = csv.reader(nutrition_csv)
        next(rows, None)
        for row in rows:
            Nutrition.objects.update_or_create(
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
    print(rows)


def execute_diet_db():
    from dietapp.models import Diet
    from django.conf import settings
    DIET_DB = os.path.join(settings.DB_DIR, 'diet.csv')

    with open(DIET_DB, 'r', encoding='UTF-8') as diet_csv:
        rows = csv.reader(diet_csv)
        next(rows, None)
        for i, row in enumerate(rows):
            Diet.objects.update_or_create(
                food_list = row[1],
                energy = row[2],
                carb = row[3],
                protein = row[4],
                fat = row[5],
                vitamin_a = row[6],
                riboflavin = row[7],
                calcium = row[8],
                iron = row[9],
                defaults={'diet_name': f'식단 {i}'}
            )
    print(rows)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dinut.settings.local')
    settings_module = [param for param in sys.argv if '--settings' in param]
    if settings_module:
        os.environ['DJANGO_SETTINGS_MODULE'] = settings_module[0].replace('--settings=','')
    django.setup()
    execute_nutrition_db()
    execute_diet_db()

if __name__ == '__main__':
    main()
