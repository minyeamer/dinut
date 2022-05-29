"""
Django settings for dinut project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, environ, json
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'accountapp',
    'profileapp',
    'dietapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dinut.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dinut.wsgi.application'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kor'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT_URL = '.'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT_URL = '.'


# Redirect urls

LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')


# Predict models

MODEL_ROOT = os.path.join(BASE_DIR, 'model')

DL_MODELS = dict()

from torch import hub
try:
    YOLO_HOME = os.path.join(MODEL_ROOT, 'ultralytics/yolov5')
    YOLO_WEIGHT = os.path.join(MODEL_ROOT, 'yolov5s.pt')
    hub.set_dir(MODEL_ROOT)
    DL_MODELS['YOLOv5'] = hub.load(YOLO_HOME, model='custom', source='local', path=YOLO_WEIGHT)
except:
    print('yolov5 model not found, load from remote')
    DL_MODELS['YOLOv5'] = hub.load('ultralytics/yolov5', 'yolov5s.pt')

try:
    from tensorflow.keras.models import load_model as load_keras_model
    DL_MODELS['InceptionV3'] = load_keras_model(os.path.join(MODEL_ROOT, 'inceptionv3.h5'))
except:
    print('keras model not found, continue without keras')
    DL_MODELS['InceptionV3'] = None


# Food labels

DB_DIR = os.path.join(BASE_DIR, 'script')
LABEL_PATH = os.path.join(DB_DIR, 'label.json')

with open(LABEL_PATH, 'r', encoding='UTF-8') as json_data:
    LABEL = json.load(json_data)
