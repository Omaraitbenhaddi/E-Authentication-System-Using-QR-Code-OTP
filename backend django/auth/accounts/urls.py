from django.urls import re_path
from .views import LoginAPI, LogoutView, ValidateEmailSendOTP,Validateotp, Welecom
app_name='accounts'
urlpatterns = [
    re_path(r'validate/', ValidateEmailSendOTP.as_view()),
    re_path(r'validate_otp/',Validateotp.as_view()),
    re_path(r'login/',LoginAPI.as_view()),
    re_path(r'logout/',LogoutView.as_view()),
    re_path(r'myaccount/',Welecom.as_view()),  
]

