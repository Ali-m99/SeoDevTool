import os
import awsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SeoDevTool.settings')
application = get_wsgi_application()

def handler(event, context):
    return awsgi.response(application, event, context) 