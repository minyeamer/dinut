from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Predict models

MODEL_ROOT = os.path.join(BASE_DIR, 'model')

DL_MODELS = dict()

print(os.listdir(BASE_DIR))
print(os.listdir(MODEL_ROOT))

from torch import hub
# try:
# load yolov5, if yolov5 repository and weight exist in local
YOLO_HOME = os.path.join(MODEL_ROOT, 'ultralytics/yolov5')
print(os.listdir(YOLO_HOME))
YOLO_WEIGHT = os.path.join(MODEL_ROOT, 'yolov5s.pt')
hub.set_dir(MODEL_ROOT)
DL_MODELS['YOLOv5'] = hub.load(YOLO_HOME, model='custom', source='local', path=YOLO_WEIGHT)
# except:
#     # if not, load yolov5 from remote
#     print('yolov5 model not found')
#     DL_MODELS['YOLOv5'] = hub.load('ultralytics/yolov5', 'yolov5s.pt')

# load keras model, if keras model exists in local
from tensorflow.keras.models import load_model as load_keras_model
DL_MODELS['InceptionV3'] = load_keras_model(os.path.join(MODEL_ROOT, 'inceptionv3.h5'))

DB_DIR = os.path.join(BASE_DIR, 'script')
LABEL_PATH = os.path.join(DB_DIR, 'label.json')
