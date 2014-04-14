#!/usr/bin/env python
import os
import sys
path='/var/www/SocialNwk'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'SocialNwk.settings_tuo_aws'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()