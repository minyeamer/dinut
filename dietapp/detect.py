from django.conf import settings
from typing import List, Optional
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import pandas as pd

STATIC_DIR = settings.STATIC_ROOT_URL + settings.STATIC_URL
FONT = ImageFont.truetype(STATIC_DIR + 'fonts/NanumSquareB.otf', size=16)


def detect_food(image_url: str, bbox: Optional[bool] = True) -> List[str]:

    diet_image = cv2.imread(image_url)
    bowls = detect_bowls(diet_image)
    bbox_list, food_list = list(), list()

    if len(bowls) > 0:
        for bowl in bowls.iterrows():
            xmin, ymin, xmax, ymax = list(map(int,(bowl[1].tolist()[:4])))
            result = predict_food(diet_image[ymin:ymax, xmin:xmax])
            if result:
                bbox_list.append(list(map(int,[xmin,ymin,xmax,ymax]))+[result])
            food_list.append(result)
        if bbox:
            draw_bbox(image_url, bbox_list)
    else:
        food_list.append(predict_food(diet_image))

    return sorted(food_list)


def detect_bowls(diet_image: np.ndarray) -> pd.DataFrame:

    model = settings.DL_MODELS['YOLOv5']

    results = model(diet_image, size=328)
    boxes = results.pandas().xyxy[0]

    return boxes[boxes.name == 'bowl']


def predict_food(food_image: np.ndarray) -> str:
    model = settings.DL_MODELS['InceptionV3']

    if model is not None:
        food_image = cv2.resize(food_image, (299,299))
        food_image = np.expand_dims(food_image, axis=0)
        food_preds = model.predict(food_image)
        label_index = np.argmax(food_preds)
        label = settings.LABEL[str(label_index)]
    else:
        import random
        label = random.choice(list(settings.LABEL.values()))

    return label


def draw_bbox(image_url: str, bbox_list: List[List[float]]):

    diet_image = cv2.imread(image_url)

    for xmin, ymin, xmax, ymax, name in bbox_list:
        cv2.rectangle(diet_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        Y = ymin - 10 if ymin - 10 > 10 else ymin + 10
        diet_image = Image.fromarray(diet_image)
        draw = ImageDraw.Draw(diet_image)

        draw.text((xmin, Y), name, (0,255,0), FONT, stroke_width=2, stroke_fill=(0,0,0))
        diet_image = np.array(diet_image)

    cv2.imwrite(image_url, diet_image)
