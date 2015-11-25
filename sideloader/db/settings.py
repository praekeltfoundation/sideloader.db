SECRET_KEY = "ChangeMe"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sideloader',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INSTALLED_APPS = (
    'sideloader.db',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'social.apps.django_app.default',
)

TIME_ZONE = 'UTC'
