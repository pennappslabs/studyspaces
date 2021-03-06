# Django settings for studyspaces project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
from sandbox_config import DATABASE_PASSWORD

# making template path relative to allow for modular development
# thanks http://komunitasweb.com/2010/06/relative-path-for-your-django-project/
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# Default values are Penn Labs specific
# Change based on specific server configuration
ADMINS = (
    ('Penn Labs', 'admin@pennlabs.org'),
)
SERVER_EMAIL = "admin+studyspaces@pennlabs.org"

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'studyspaces',             # Or path to database file if using sqlite3.
        'USER': 'studyspaces',             # Not used with sqlite3.
        'PASSWORD': DATABASE_PASSWORD,         # Not used with sqlite3. SET IN SANDBOX_CONFIG
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

from sandbox_config import * # may override DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH + '/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/%s/media/' % (DISPLAY_NAME)

# Make this unique, and don't share it with anybody.
#SECRET_KEY = None # SET IN SANDBOX_CONFIG

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


ROOT_URLCONF = 'studyspaces.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'media/front-end'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'app',
    'south',
)
