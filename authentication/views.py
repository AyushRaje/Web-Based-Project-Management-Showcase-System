from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt,csrf_protect,requires_csrf_token,ensure_csrf_cookie
import os
from decouple import config
from asgiref.sync import sync_to_async
from database.checks.check_referral import check_referral_code 
from database.saves.create_org import create_organization,generate_referral_code
from adrf.decorators import api_view
# Create your views here.
@csrf_exempt
@api_view(['GET'])
async def ping(request):
    if request:
        response = {
            "status":True,
            "response":"successful"
        }
    else:
        response = {
            "status":False,
            "response":"failed"
        }    
    return Response(response)
@api_view(['GET'])
async def get_csrf(request):
    status = "Success"
    try:
        token = await sync_to_async(get_token,thread_sensitive=True)(request)
    except Exception as e:
        status = "Exception in get token :"+str(e)
        token = ""     
    return Response({
        "status":status,
        "X-CSRFToken":token
    })

@csrf_protect
@api_view(['POST'])
async def create_org(request):
    status = "Success"
    org_id = ""
    name = request.POST.get('name',None)
    city = request.POST.get('city',None)
    referral = request.POST.get('referral',None)
    type = request.POST.get('type','Private')
    try:
        check,status = await check_referral_code(referral=referral)
        if check:
            status,org_id = await create_organization(name=name,city=city,referral=referral,type=type)
        else:
            status = "Invalid Referral"
    except Exception as e:
        status = "Exception in create_org:"+str(e)
        print(status)
    return Response({
        "status":status,
        "org_id":org_id,
        "referral":referral
    })                

@csrf_protect
@requires_csrf_token
@api_view(['POST'])
async def generate_referral(request):
    status = "Success"
    user_key = request.POST.get('user_key','')
    referral = ""
    try:
        if user_key == config('USER_KEY'):
           referral = await generate_referral_code()
        else:
            status = "Invalid User key"
            referral = ""
    except Exception as e:
        status = "Exception in generate referral: "+str(e)
        print(status)
    return Response({
       "status":status,
       "referral":referral 
    })
@csrf_protect
@requires_csrf_token
@api_view(['GET'])
async def test_api(request):
    status = "Success"
    try:
        pass
    except Exception as e:
        status = "Exception in test api: "+str(e)
        print(status)
    return Response({
       "status":status,
       "api_gateway":'active'
    })        