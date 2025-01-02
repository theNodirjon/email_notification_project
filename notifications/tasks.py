from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_admin_email():
    send_mail(
        'Kunlik Xabarlar Hisoboti',
        'Bu xat barcha foydalanuvchi xabarlari ro‘yxati haqida.',
        'testabsd2@gmail.com',
        ['testabsd2@gmail.com'],
    )