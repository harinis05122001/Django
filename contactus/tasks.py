from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_mail_task(subject, message, from_email, recipient_mail):
    send_mail(subject, message, from_email, recipient_mail)