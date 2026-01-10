from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_email_about_update_the_course_materials(email, subject, message):
    """Асинхронная рассылка писем всем подписчикам курса об обновлении."""
    send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
