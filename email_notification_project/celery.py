from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django loyihasi uchun standart sozlamalar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_notification_project.settings')

app = Celery('email_notification_project')

# Django sozlamalarini ishlatish
app.config_from_object('django.conf:settings', namespace='CELERY')

# Vazifalarni avtomatik yuklash
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
