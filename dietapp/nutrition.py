from typing import DefaultDict, Dict, List
from django.conf import settings
from dietapp.models import Nutrition
from django.db.models import Sum
from dietapp.detect import detect_food
from collections import defaultdict

NUTRITIONS = ['energy','carb','protein','fat','sugar','fiber',
            'sodium','vitamin_a','riboflavin','calcium','iron']


def analyze_diet(image_url: str) -> Dict[str, float]:
    detect_result = dict()
    food_list = detect_food(settings.MEDIA_ROOT_URL + image_url)
    nutrition_rows = Nutrition.objects.filter(food_name__in=food_list)

    detect_result['food_list'] = ', '.join(food_list)
    for nutrition in NUTRITIONS:
        detect_result[nutrition] = list(nutrition_rows.aggregate(Sum(nutrition)).values())[0]

    return detect_result


def sum_nutritions(image_urls: List[str]) -> DefaultDict[str, float]:
    calc_result = defaultdict(int)

    for image_url in image_urls:
        detect_result = analyze_diet(settings.MEDIA_ROOT_URL + image_url)

        for nutrition in NUTRITIONS:
            calc_result[nutrition] += detect_result[nutrition]

    return calc_result
