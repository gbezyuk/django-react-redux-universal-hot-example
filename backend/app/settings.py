"""
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

# For production settings checklist, see
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
"""

# Entry point for url dispatching
ROOT_URLCONF = 'app.urls'

# Entry point to run as WSGI app
WSGI_APPLICATION = 'app.wsgi.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
CORS_ORIGIN_ALLOW_ALL = True

# For internationalization settings, see
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# For database settings see
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images; used by admin panel apps)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (like uploaded images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INSTALLED_APPS = (
    'django.contrib.contenttypes',

    'grappelli.dashboard',
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django_extensions',
    'ordered_model',
    'corsheaders',
    'rest_framework',

    'app',
    'pages',
    'photos',
    'api',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd@7r&u1uk1o$ie3ybtkepwoc#8vcgd_x7g*u395w%%4n+7e*-v'

FILEBROWSER_VERSIONS_BASEDIR = '_versions'
FILEBROWSER_VERSIONS = {
  'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 320, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['admin_thumbnail']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    )
}

GRAPPELLI_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'
