import email
from urllib import request
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.response import Response
from .models import User , EmailOTP
from .serializer import LoginUserSerializer
from django.contrib.auth.signals import  user_logged_out
import random

from rest_framework import permissions,status
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView


class ValidateEmailSendOTP(APIView):    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)





    def post(self,request,*args,**kwargs):
        email_get =request.data.get('email')
        if email_get:
            email=str(email_get)
            user = User.objects.filter(email__iexact = email)
            if user.exists():
                return Response({
                    'status':False,
                    'detail':'email number already exists'
                })
            else:
                key=send_otp(email)
                if key:
                    old=EmailOTP.objects.filter(email__iexact = email)
                    if old.exists():
                        old=old.first()
                        count=old.count
                        if count>10:
                                            return Response({
                                                                'status':False,
                                                                'detail':'sending otp error. limit exceded please contact customer suport'
                                                            })
                        old.count=count+1
                        old.otp=key
                        old.save()
                        return Response({
                            'status': True,
                            'detail':'sent otp seccuful'
                        })

                    else :


                        EmailOTP.objects.create(
                            email=email,
                            otp=key,

                        )
                        return Response({
                            'status': True,
                            'detail':'sent otp seccuful'
                        })
                else :
                    return Response({
                        'status':False,
                        'detail':'sending otp eror'
                    })




        else:
            return Response({
                'status':False,
                'detail':'email number not given in post request'
            })



class Validateotp(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    
    def post(self,request,*args,**kwargs):
        email = request.data.get('email',False)
        otp_sent =  request.data.get('otp',False)

        if email and otp_sent:
            old=EmailOTP.objects.filter(email__iexact=email)
            if old.exists():
                old= old.first()
                otp=old.otp
                if str(otp)==str(otp_sent):
                    old.validated = True
                    old.save()

                    return Response({
                        'status':True,
                        'detail':"otp matched kindly process to save password"
                    })

                else:
                    return Response({
                        'status':False,
                        'detail':'OTP incorect please try again'
                    })

            else :
                return Response({
                    'status':False,
                    'detail':'Either email or otp was not recieved in Post request' 
                })






class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request , user)
        return super().post(request , format=None)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)








def send_otp(email):
    if email:
        key=random.randint(999,9999)
        email=str(email)
       # /// cette partie ajouter sending mail
        print(key)
        return key
    else:
        return False