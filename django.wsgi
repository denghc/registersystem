import os
import sys
import django.core.handlers.wsgi
sys.path.append('E:/DjangoWorkSpace')
sys.path.append('E:/DjangoWorkSpace/RegisterSystem')
os.environ['DJANGO_SETTINGS_MODULE'] = 'RegisterSystem.settings'
application = django.core.handlers.wsgi.WSGIHandler() 