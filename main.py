#!/usr/bin/env python
# encoding: utf-8


import os
import sys
from django.core.wsgi import get_wsgi_application


PATH_TO_PROJECT = '/Users/Vegeta/Documents/pythonspace/fangSpider/'
sys.path.extend([PATH_TO_PROJECT, ])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fangSpider.settings")
application = get_wsgi_application()

from fspider import views

views.spide_house_info()
# views.collect_all_urls()
# views.test_collect_one()
