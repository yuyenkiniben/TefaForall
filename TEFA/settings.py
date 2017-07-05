
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vrp@x%i=z%j@rff_6^fq1ozzyt8nv!kx*d870u_v^c2y0qoug3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    # rating stars
    'star_ratings',
    'Core',
    'Concours',
    'rest_framework',
    'latexify',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TEFA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Already defined Django-related contexts here
                # 'allauth' requires the request context processor
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'TEFA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")  # this is to create a virtual network on which we will have our static files

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")  # this is to create a virtual network on which we will have our static files


# **************** Django Allauth ******************

# Add the 'allauth' backend to AUTHENTICATION_BACKEND and do not remove ModelBackend
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin and to ensure compatibility with other packages
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Ensure the SITE_ID is defined
SITE_ID = 1

# Ensure EMAIL_BACKEND is set so allauth can proceed to send confirmation emails
# Set to console for development/testing



# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/Logout'
LOGIN_REDIRECT_URL = '/'

# *********** Social Media ********************

SOCIALACCOUNT_PROVIDERS = {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERSION': 'v2.4'},
        'google': { 'SCOPE': ['email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
        }
}

# ************************* Adding userprofile model ***************

# Adding a new field into the standard django user model

AUTH_PROFILE_MODULE = "Core.UserProfile"

# ******************* Star Ratings ****************************

STAR_RATINGS_STAR_HEIGHT = 15
STAR_RATINGS_STAR_WIDTH = 15
STAR_RATINGS_RERATE = False


# ***************** Emails sending **********************
# Email configuration.
#For email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'forall.afrik@gmail.com'

#Must generate specific password for your app in [gmail settings][1]
EMAIL_HOST_PASSWORD = 'Africa_For_All2020'

EMAIL_PORT = 587

#This did the trick
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
