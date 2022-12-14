import email
from urllib import request
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.response import Response
from .models import User , EmailOTP
from django.shortcuts import get_object_or_404
from .serializer import LoginUserSerializer, UserSerializer
from django.contrib.auth.signals import  user_logged_out
from rest_framework.decorators import api_view
import random,math
from .emails import *

from rest_framework import permissions,status
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView

class Welecom(APIView):
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,) 
    def post(self, request):
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            #serializer.save()
            email = serializer.data['email']
            username = serializer.data['name']
            otp_user=EmailOTP.objects.filter(email__iexact = email)
            if otp_user.exists():
                    otp_user_att=otp_user.first()
                    
                    if not otp_user_att.validated:
                        return Response({
                            'status':400,
                            'detail': 'you have to validate your otp'
                        })
                    if email :
                        count=otp_user_att.count
                        return Response({
                            'status': 200,
                            'detail':{"email":email,"username":username,"count":count}
                        })
            else:
                        return Response({
                            'status': 400,
                            'detail':"user not exists"
                        })
        else:
            return Response({
                'status':400,
                'detail':'something went wrong check your account information',
                'data': serializer.errors
            })

class ValidateEmailSendOTP(APIView):
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request,*args,**kwargs):
        data=request.data
        email = data.get('email')
        if email:
            user = User.objects.filter(email__iexact = email)
            key=send_otp_email(email)
            if key:
                old=EmailOTP.objects.filter(email__iexact = email)
                if old.exists():
                    old=old.first()
                    count=old.count
                    if count>10:
                        return Response({
                            'status':400,
                            'detail':'sending otp error. limit exceded please contact customer suport'
                        })
                    old.count=count+1
                    old.otp=key
                    old.save()
                    return Response({
                        'status': 200,
                        'detail':'sent otp seccuful'
                    })
                else : 
                    EmailOTP.objects.create(
                        email=email,
                        otp=key,
                    )
                    return Response({
                            'status': 200,
                            'detail':'sent otp seccuful'
                        })
            else :
                    return Response({
                        'status':400,
                        'detail':'sending otp eror'
                    })
        else:
            return Response({
                'status':400,
                'detail':'something went wrong'

            })



class Validateotp(APIView):
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        data = request.data
        email = data.get('email')
        otp_sent = data.get('otp')
        if email and otp_sent:
            old=EmailOTP.objects.filter(email__iexact=email)
            if old.exists():
                old= old.first()
                otp=old.otp
                if otp == otp_sent:
                    old.validated = True
                    old.save()
                    return Response({
                        'status':200,
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
        return Response({
            'status' : False,
            'detaild' : 'something went wrong'
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
