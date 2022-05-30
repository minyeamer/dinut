from typing import DefaultDict, Dict, List
from django.conf import settings
from django.db.models import Sum
from dietapp.models import Nutrition, Diet, DietImage
from dietapp.detect import detect_food
from dietapp.fusioncharts import FusionCharts
from collections import OrderedDict, defaultdict
import pandas as pd
from datetime import datetime

NUTRITIONS = ['energy','carb','protein','fat','sugar','fiber',
            'sodium','vitamin_a','riboflavin','calcium','iron']
MACRONUTRIENTS = ['carb','protein','fat']


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
        detect_result = analyze_diet(image_url)

        for nutrition in NUTRITIONS:
            calc_result[nutrition] += detect_result[nutrition]

    return calc_result


def get_nutrition_charts(id: str) -> List[str]:
    diet_info = DietImage.objects.filter(id=id).values(
        'energy','carb','protein','fat','sugar','fiber',
        'sodium','vitamin_a','riboflavin','calcium','iron')[0]

    data_source = OrderedDict()
    data_source['data'] = [{'label':label,'value':value}
        for label,value in diet_info.items() if label in MACRONUTRIENTS]

    chart_config = OrderedDict()
    chart_config['caption'] = '탄단지 그래프'
    chart_config['xAxisName'] = '영양 성분'
    chart_config['yAxisName'] = 'g'
    chart_config['numberSuffix'] = 'K'
    chart_config['theme'] = 'fusion'

    data_source['chart'] = chart_config

    column2D = FusionCharts('column2d','columnChart','600','400','chart-col','json',data_source).render()
    pie2D = FusionCharts('pie2d','pieChart','600','400','chart-pie','json',data_source).render()
    stackedBar2D = FusionCharts('stackedarea2d','stackedBarChart','600','400','chart-bar','json',data_source).render()
    return [column2D, pie2D, stackedBar2D]


def get_similar_diet(id: int) -> str:
    diet_table = Diet.objects.all().values('id','energy','carb','protein','fat')
    diet_df = pd.DataFrame(diet_table)
    target = Diet.objects.filter(pk=id).values('id','energy','carb','protein','fat')[0]
    nut_ratios = [f'{macronutrition}_ratio' for macronutrition in MACRONUTRIENTS]

    target.update({nut_ratios[i]:(round(target[MACRONUTRIENTS[i]]/target['energy'],2)
                    if target['energy'] > 0.0 else 0.0) for i in range(len(MACRONUTRIENTS))})

    for i in range(len(MACRONUTRIENTS)):
        diet_df[nut_ratios[i]] = round(diet_df[MACRONUTRIENTS[i]].div(diet_df['energy']),2)

    diet_df['diff_cal'] = abs(diet_df['energy']-target['energy'])
    diet_df['diff_nut'] = sum([abs(diet_df[nut]-target[nut]) for nut in MACRONUTRIENTS])
    diet_df['diff_ratio'] = sum([abs(diet_df[nut_ratio]-target[nut_ratio])
                                for nut_ratio in nut_ratios])

    diet_df.drop(['energy']+MACRONUTRIENTS+nut_ratios,axis=1,inplace=True)
    diet_df.sort_values(['diff_cal','diff_ratio','diff_nut'],inplace=True)

    similar_id = diet_df.head()['id'].tolist()
    similar_list = Diet.objects.filter(id__in=similar_id).values(
                                        'food_list','energy','carb','protein','fat')
    kr_dict = {'food_list':'식품 목록', 'energy':'칼로리(kcal)',
                'carb':'탄수화물(g)', 'protein':'프로틴(g)', 'fat':'지방(g)'}
    similar_df = pd.DataFrame(similar_list).rename(kr_dict, axis=1)
    return similar_df.set_index('식품 목록').to_html(classes='table table-striped text-center', justify='center')

def get_date_fommater(target_date):
    return {'year': target_date[:4], 'month':target_date[5:7], 'day':target_date[8:10],'target_date':target_date}

def string_to_date(datetime_string):
    query_date = datetime.strptime(datetime_string, '%Y-%m-%d')
    return query_date
     