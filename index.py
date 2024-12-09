import awsgi
from SeoDevTool.wsgi import application

def handler(event, context):
    return awsgi.response(application, event, context) 