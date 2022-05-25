from django.conf import settings
from typing import List
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import pandas as pd


def analyze_diet(image_url: str) -> List[str]:
    image = cv2.imread(image_url)
    bowls = detect_bowls(image)
    bbox_list, food_list = list(), list()
    import random # InceptionV3 모델 완성 전 디버깅용 코드
    debug = ['밥','닭가슴살','가츠동','감자튀김','국수'] # InceptionV3 모델 완성 전 디버깅용 코드

    if len(bowls) > 0:
        for bowl in bowls.iterrows():
            xmin, ymin, xmax, ymax, _, _, _ = bowl[1].tolist()
            # result = detect_food(image[xmin:xmax, ymin:ymax])
            result = random.choice(debug) # InceptionV3 모델 완성 전 디버깅용 코드
            bbox_list.append(list(map(int,[xmin,ymin,xmax,ymax]))+[result])
            food_list.append(result)
        draw_bbox(image_url, bbox_list)
        return food_list
    else:
        # result = detect_food(image)
        result = random.choice(debug) # InceptionV3 모델 완성 전 디버깅용 코드
        return [result]


def detect_bowls(image: np.ndarray) -> pd.DataFrame:
    model = settings.DL_MODELS['YOLOv5']

    results = model(image, size=328)
    boxes = results.pandas().xyxy[0]

    return boxes[boxes.name == 'bowl']


def detect_food(image: np.ndarray) -> str:
    model = settings.DL_MODELS['InceptionV3']
    result = None

    return result


def draw_bbox(image_url: str, bbox_list: List[List[float]]):
    image = cv2.imread(image_url)

    for xmin, ymin, xmax, ymax, name in bbox_list:
        # rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        Y = ymin - 10 if ymin - 10 > 10 else ymin + 10
        image = Image.fromarray(image)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('.'+settings.STATIC_URL+'fonts/NanumSquareB.otf', size=16)
        draw.text((xmin, Y), name, (0,255,0), font, stroke_width=2, stroke_fill=(0,0,0))
        image = np.array(image)
        # putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        # cv2.putText(image, name, (xmin, Y), font, 0.7, (0, 255, 0), 2)

    cv2.imwrite(image_url, image)
