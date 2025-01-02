from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import UserNotification

@receiver(post_save, sender=UserNotification)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Yangi Xabar Keldi",
            message=f"Salom {instance.name},\n\n{instance.message}",
            from_email='admin@example.com',
            recipient_list=[instance.email],
        )
