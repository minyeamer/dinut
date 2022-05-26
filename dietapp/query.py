from typing import DefaultDict, Dict, List
from django.conf import settings
from django.db.models import Sum, F
from dietapp.models import Nutrition, Diet
from dietapp.detect import detect_food
from collections import defaultdict
import pandas as pd

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


def get_similar_diet(id: int) -> dict:
    diet_table = Diet.objects.all().values('id','energy','carb','protein','fat')
    diet_df = pd.DataFrame(diet_table)
    target = Diet.objects.filter(pk=id).values('id','energy','carb','protein','fat')[0]
    nuts = ['carb','protein','fat']
    nut_ratios = [f'{nutrition}_ratio' for nutrition in nuts]

    target.update({nut_ratios[i]:(round(target[nuts[i]]/target['energy'],2)
                    if target['energy'] > 0.0 else 0.0) for i in range(len(nuts))})

    for i in range(len(nuts)):
        diet_df[nut_ratios[i]] = round(diet_df[nuts[i]].div(diet_df['energy']),2)

    diet_df['diff_cal'] = abs(diet_df['energy']-target['energy'])
    diet_df['diff_nut'] = sum([abs(diet_df[nut]-target[nut]) for nut in nuts])
    diet_df['diff_ratio'] = sum([abs(diet_df[nut_ratio]-target[nut_ratio])
                                for nut_ratio in nut_ratios])

    diet_df.drop(['energy']+nuts+nut_ratios,axis=1,inplace=True)
    diet_df.sort_values(['diff_cal','diff_ratio','diff_nut'],inplace=True)

    return diet_df.head()['id'].tolist()
