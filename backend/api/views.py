from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    data = {"message": "This is the message!"}
    return JsonResponse(data=data)