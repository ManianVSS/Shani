import os
from pathlib import Path

import django_env_overrides
import yaml
from django.conf.global_settings import FORCE_SCRIPT_NAME
from tutorial.settings import ALLOWED_HOSTS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9=(@6%n=2c^$4%b1-0!7-k+=vjeo8pub3r&$$ijw(0tchsaxn4'

# Read config.yaml config file if it exists
if os.path.exists(os.path.join(BASE_DIR, 'config.yaml')):
    with open(os.path.join(BASE_DIR, 'config.yaml'), 'r') as stream:
        config = yaml.safe_load(stream)
else:
    config = {
        'LOG_FILE': 'logs/server.log',
        'LOG_LEVEL': 'INFO',

        'DEBUG': True,

        'FQDN': '*',
        'ALLOWED_HOSTS': ['*'],

        'FORCE_SCRIPT_NAME': '',
        'TEMPLATES_DIRS': ['build', 'templates'],
        'DATA_MOUNT_DIR': str(BASE_DIR),

        'STATIC_FILES': ['static', 'build', 'build/static', 'build/assets', ],
        'STATIC_URLS': ['/static/', 'assets/'],
        'MEDIA_URL': '/data/',

        'LANGUAGE_CODE': 'en-us',
        'USE_I18N': True,
        'USE_TZ': True,
        'TIME_ZONE': 'Asia/kolkata',  # UTC

        'DATABASE': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(Path(BASE_DIR, 'data', 'db.sqlite3')),
        },
    }

LOG_FILE = config['LOG_FILE'] if 'LOG_FILE' in config else 'logs/server.log'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
LOG_LEVEL = config['LOG_LEVEL'] if 'LOG_LEVEL' in config else 'INFO'

APP_LOGGER = {
    "handlers": ["console", "file"],
    "level": LOG_LEVEL,
    "propagate": True,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": LOG_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
            "filename": LOG_FILE,
            "formatter": "verbose",
        },
    },

    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {process:d} {thread:d} [{name}:{lineno}]: {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },

    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
        "test_mgmt": APP_LOGGER,
        "api": APP_LOGGER,
        "automation": APP_LOGGER,
        "execution": APP_LOGGER,
        "people": APP_LOGGER,
        "program": APP_LOGGER,
        "requirements": APP_LOGGER,
        "scheduler": APP_LOGGER,
        "siteconfig": APP_LOGGER,
        "testdesign": APP_LOGGER,
        "workitems": APP_LOGGER,
    }
}

print("Config used is:", str(config))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config['DEBUG'] if 'DEBUG' in config else True

FQDN = config['FQDN'] if 'FQDN' in config else '*'

ALLOWED_HOSTS = config['ALLOWED_HOSTS'] if 'ALLOWED_HOSTS' in config else ['*']

DATA_MOUNT_DIR = config['DATA_MOUNT_DIR'] if 'DATA_MOUNT_DIR' in config else str(BASE_DIR)
os.makedirs(str(Path(DATA_MOUNT_DIR, "data")), exist_ok=True)

X_FRAME_OPTIONS = 'SAMEORIGIN'
# APPEND_SLASH = False

USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = config['FORCE_SCRIPT_NAME'] if 'FORCE_SCRIPT_NAME' in config else ''

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
        'DIRS': [os.path.join(BASE_DIR, template_dir) for template_dir in
                 config['TEMPLATES_DIRS']] if 'TEMPLATES_DIRS' in config else
        [os.path.join(BASE_DIR, 'build'), os.path.join(BASE_DIR, 'templates'), ],

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

DATABASES = {
    "default": config['DATABASE'] if 'DATABASE' in config else {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(Path(DATA_MOUNT_DIR, 'data', 'db.sqlite3')),
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

STATIC_SUFFIXIES = config['STATIC_URLS'] if 'STATIC_URLS' in config else ['/static/', '/assets/']
STATIC_URLS = [FORCE_SCRIPT_NAME + STATIC_URL for STATIC_URL in STATIC_SUFFIXIES]
MEDIA_SUFFIX = '/data/'
MEDIA_URL = config['MEDIA_URL'] if 'MEDIA_URL' in config else FORCE_SCRIPT_NAME + MEDIA_SUFFIX

static_file_dir_config = config['STATIC_FILES'] if 'STATIC_FILES' in config else ['static', 'build', 'build/static',
                                                                                  'build/assets', ]
STATICFILES_DIRS = [str(Path(BASE_DIR, static_file_dir)) for static_file_dir in static_file_dir_config]

for STATIC_URL in STATIC_URLS:
    STATICFILES_DIRS.append(str(Path(BASE_DIR, STATIC_URL)))

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_BASE_NAME = 'data'
MEDIA_ROOT = str(Path(DATA_MOUNT_DIR, MEDIA_BASE_NAME))
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
DBBACKUP_CLEANUP_KEEP = 30
DBBACKUP_CLEANUP_KEEP_MEDIA = 30
# DBBACKUP_HOSTNAME = os.getenv('HOSTNAME', 'localhost')

os.makedirs(os.getenv('HOME', ".") + '/backup/Shani/dbbackup', exist_ok=True, )

CRONJOBS = [
    ('0 */6 * * *', 'test_mgmt.db_backup_cronjob.backup')
]

JAZZMIN_SETTINGS = {
    "show_ui_builder": True,
    "site_logo": "raven.png",
    "login_logo": "raven.png",
}

# ATTACHMENT_DIR = "./attachments"
# os.makedirs(ATTACHMENT_DIR, exist_ok=True)
django_env_overrides.apply_to(globals())
