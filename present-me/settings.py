"""
Django settings for oscartest project.

Generated by 'django-admin startproject' using Django 1.9.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from oscar import get_core_apps
from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = BASE_DIR

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '.'))

TEMPLATE_DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(**ao)goj9%y=bzbk3(ky_f(q&9i14gyqo_@avzy4_nd3_q(pb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'present-me.com.ua',
    'www.present-me.com.ua',
    'dev.present-me.com.ua',
    'www.dev.present-me.com.ua',
]


"""
Это настройки модуля django-compressor, предназначенного для склейки и
сжатия JS и CSS
Сайт проекта: http://django-compressor.readthedocs.org/en/latest/
Небольшая заметка на русском: http://vorushin.ru/blog/33-django-compressor/
"""
COMPRESS_ROOT = BASE_DIR  # TODO: разобраться подробнее с компрессором и этой настройкой

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.flatpages',
    'django.contrib.sites',
    'compressor',
    'widget_tweaks',

    'main',
] + get_core_apps([
    'apps.promotions',
    'apps.shipping',
                   ])
#
SITE_ID = 1
#1
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]
AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'present-me.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'present-me.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'present-me',
    'USER': 'postgres',
    'PASSWORD': 'workfree',
    'HOST': 'localhost', # Set to empty string for localhost.
    'PORT': '5432', # Set to empty string for default.
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = False
USE_TZ = True

"""
Если параметр LANGUAGES не указан, в левом верхнем углу страницы будет
отображаться выпадающий список со всеми поддерживаемыми языками перевода
интерфейса магазина.
Если указать единственный язык - выпадающий список не будет отображаться вообще.
Если указать несколько языков, то список будет содержать только их.
"""
LANGUAGES = (
    ('ru', 'Russian'),
    ('uk', 'Ukrainian'),
)
LANGUAGE_CODE = 'ru'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#         'URL': 'http://127.0.0.1:8983/solr',
#         'INCLUDE_SPELLING': True,
#     },
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static',),
]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static')

SERVER_EMAIL = 'admin@example.com'
#Настройки магазина
OSCAR_SHOP_NAME = '"Present Me"'
OSCAR_SHOP_TAGLINE = u'лучшее место для покупок в сети'
OSCAR_DEFAULT_CURRENCY = 'UAH'
OSCAR_CURRENCY_LOCALE = 'ru_RU'
"""
OSCAR_REQUIRED_ADDRESS_FIELDS определяет обязательные поля при оформлении
заказа.
С точки зрения покупателя, меня бесит необходимость заполнять поля,
которые не нужны. Зачем, например, обязывать заполнять адрес доставки,
если я хочу забрать покупку самовывозом?
Поэтому оставляйте только действительно необходимое.
"""
OSCAR_REQUIRED_ADDRESS_FIELDS = (
    'first_name',
#    'last_name',
#    'line1',
#    'line4',
#    'postcode', #  TODO: все равно требует ввести индекс, хоть и не помечает, как обязательное
#    'country',
    )
OSCAR_PRODUCTS_PER_PAGE = 20  # количество товаров на странице
OSCAR_ALLOW_ANON_CHECKOUT = False  # разрешить покупки без регистрации
OSCAR_ALLOW_ANON_REVIEWS = True  # разрешить анонимные отзывы о товаре
OSCAR_MODERATE_REVIEWS = False  # проверка отзывов перед публикацией на сайте
"""
Следующий параметр разрешает немедленную отсылку уведомлений о поступившем
товаре покупателям, которые просили их уведомить. Может создавать значительную
нагрузку на сервер при больших объемах рассылки. не рекомендуется использовать.
Подробнее смотрите в документации.
"""
OSCAR_EAGER_ALERTS = True
"""
Следующий параметр определяет, надо ли отсылать покупателям уведомление о
регистрации в магазине. Стоит отметить, что подтверждения регистрации не
требуется, так что отсылается только информационное уведомление.
"""
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL = 'noreply@present-me.com.ua'
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20  # количество запоминаемых недавно просмотренных товаров
OSCAR_MAX_BASKET_QUANTITY_THRESHOLD = None  # количество товаров, которые можно добавить в корзину


"""
Настройка статусов заказов.
Для каждого статуса можно указать статусы, на которые можно изменить текущий.
"""
OSCAR_INITIAL_ORDER_STATUS = u'Новый'
OSCAR_INITIAL_LINE_STATUS = u'Новый'
OSCAR_LINE_STATUS_PIPELINE = {
    u'Новый': (u'Подготовлен', u'Отменен',),
    u'Подготовлен': (u'Отгружен', u'Отменен',),
    u'Отгружен': (),
    u'Отменен': (),
}
