import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# example) SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
    }
}

# example) MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

INSTALLED_APPS = (
    'data',
)

SECRET_KEY = 'REPLACE_ME'
