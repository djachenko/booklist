from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booklist.settings')

app = Celery("booklist")

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
