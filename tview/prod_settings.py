from tview.settings import *



ALLOWED_HOSTS = ['.tview.fr']

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'