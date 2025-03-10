import os
from pathlib import Path

import django_env_overrides

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9=(@6%n=2c^$4%b1-0!7-k+=vjeo8pub3r&$$ijw(0tchsaxn4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # bool(os.getenv("DEBUG", 'True'))

FQDN = os.getenv('FQDN', "*")
if os.getenv("mode", "staging") == "production":
    ALLOWED_HOSTS = [FQDN]
else:
    ALLOWED_HOSTS = ["*"]

X_FRAME_OPTIONS = 'SAMEORIGIN'
# APPEND_SLASH = False

USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = os.getenv('FORCE_SCRIPT_NAME', '')

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django_ace',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_group_model',
    'django_crontab',
    'django_extensions',

    'rest_framework',  # Added for Django Rest Framework
    'rest_framework.authtoken',
    'rest_framework_swagger',

    'django_filters',  # Added for filtering

    'corsheaders',

    'import_export',  # Import export

    # 'advanced_filters',  # Advanced filters

    # 'guardian',

    'massadmin',

    # 'revproxy', # Reverse proxy config

    'dbbackup',  # django-dbbackup

    # Project modules
    # 'auth_custom',
    'api',
    'siteconfig',
    'requirements',
    'workitems',
    'scheduler',
    'testdesign',
    'automation',
    'execution',
    'people',
    'program',
]

# 'api.middlewares.CustomCorsMiddleware',

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_mgmt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build'), os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'api.contextprocessors.site_configuration',
            ],
            # For swagger
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'test_mgmt.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if os.getenv("mode", "staging") == "production":
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DATABASE__ENGINE', 'django.db.backends.postgresql_psycopg2'),
            'NAME': os.getenv('DATABASE__NAME', 'testmgmt'),
            'USER': os.getenv('DATABASE__USER', 'testmgmtadmin'),
            'PASSWORD': os.getenv('DATABASE__PASSWORD', 'testmgmtadmin@123'),
            'HOST': os.getenv('DATABASE__HOST', 'localhost'),
            'PORT': os.getenv('DATABASE__PORT', '5432'),
        },
        'replica': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.getenv('DATA_MOUNT_DIR', str(BASE_DIR)) + '/data/replica.sqlite3',
        },
    }
else:
    os.makedirs(os.getenv('DATA_MOUNT_DIR', str(BASE_DIR)) + '/data', exist_ok=True, )
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.getenv('DATA_MOUNT_DIR', str(BASE_DIR)) + '/data/db.sqlite3',
        },
        'replica': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.getenv('DATA_MOUNT_DIR', str(BASE_DIR)) + '/data/replica.sqlite3',
        },
    }
# print("Database object is :", str(DATABASES))
# DATABASE_ROUTERS = ['test_mgmt.database_routers.ReplicaRouter']

# AUTH_GROUP_MODEL = 'auth_custom.Group'
# AUTH_USER_MODEL = 'auth_custom.User'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'  # 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_SUFFIX = '/static/'
STATIC_URL = FORCE_SCRIPT_NAME + STATIC_SUFFIX
MEDIA_SUFFIX = '/data/'
MEDIA_URL = FORCE_SCRIPT_NAME + MEDIA_SUFFIX

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'build'),
                    os.path.join(BASE_DIR, 'build/static'),
                    os.path.join(BASE_DIR, STATIC_URL)]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_BASE_NAME = 'data'
MEDIA_ROOT = os.path.join(os.getenv('DATA_MOUNT_DIR', BASE_DIR), MEDIA_BASE_NAME)
# os.makedirs(MEDIA_ROOT, exist_ok=True)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend', # this is default
#     'guardian.backends.ObjectPermissionBackend',
# )

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],

    # Added for swagger
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # Pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPaginationExtn',
    'DEFAULT_PAGINATION_CLASS': 'api.pagination.PageNumberPaginationExtn',

    # Added for filtering
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ]

}

if os.getenv("mode", "staging") != "production":
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = [
        "accept",
        "accept-encoding",
        "authorization",
        "content-type",
        "dnt",
        "origin",
        "user-agent",
        "x-csrftoken",
        "x-requested-with",
        "access-control-allow-origin",
        "access-control-allow-methods",
        "access-control-allow-credentials",
    ]

    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]

    CORS_ALLOWED_ORIGIN_REGEXES = [
        # match localhost with any port
        r"^http:\/\/localhost:*([0-9]+)?$",
        r"^https:\/\/localhost:*([0-9]+)?$",
    ]

# DBBACKUP_DATABASES = ['default']
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.getenv('HOME', '.') + '/backup/Shani/dbbackup'}
# DBBACKUP_CLEANUP_KEEP = 30
# DBBACKUP_CLEANUP_KEEP_MEDIA = 30
# DBBACKUP_HOSTNAME = os.getenv('HOSTNAME', 'localhost')

os.makedirs(os.getenv('HOME', ".") + '/backup/Shani/dbbackup', exist_ok=True, )

CRONJOBS = [
    ('0 */6 * * *', 'test_mgmt.db_backup_cronjob.backup')
]

# ATTACHMENT_DIR = "./attachments"
# os.makedirs(ATTACHMENT_DIR, exist_ok=True)
django_env_overrides.apply_to(globals())

JAZZMIN_SETTINGS = {
    "show_ui_builder": True,
    "site_logo": "raven.png",
    "login_logo": "raven.png",
}
