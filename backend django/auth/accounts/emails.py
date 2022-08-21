from django.core.mail import send_mail
import random , math
from django.conf import settings
from .models import User

def send_otp_email(email):
    if email:
        subject = 'Your account verification email'
        cus="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        length = len(cus)
        generate_otp=""
        for i in range(10):
            generate_otp+= cus[math.floor(random.random() * length)]
        message =f'your otp is {generate_otp}'
        email_from = settings.EMAIL_HOST_USERon 
        send_mail(subject, message, email_from , [email,])
        return generate_otp
    else:
        return False