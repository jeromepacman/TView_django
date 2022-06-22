from tview.settings import *

DEBUG = False

#ALLOWED_HOSTS = ['.tview.fr', '127.0.0.1', 'localhost']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'