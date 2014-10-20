# Copyright 2008-2014 VPAC
#
# This file is part of django-pbs.
#
# django-pbs is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-pbs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-pbs  If not, see <http://www.gnu.org/licenses/>.

DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.sqlite3',
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'data.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

# Django settings for django_pbs project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jay DePasse', 'depasse@psc.edu'),
)

# A list of all PBS servers to list on the server list page
# also used when finding all jobs for a specific user.
LOCAL_PBS_SERVERS = ['fe-sandbox',]


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
STATIC_ROOT = "/home/depasse/django-pbs/static"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
STATIC_URL = '/pbs_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3498h4508vh548unv8723grikjb4c8ygb*&^RFV&pciubnm24nl5kjnl32kjh(*Y*&Y*&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.static',

    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'django_pbs.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',

    'django.contrib.staticfiles',
    'django_pbs.servers',
    'django_pbs.moab',
    'django_pbs',

    'django_extensions',
    'debug_template',
)
