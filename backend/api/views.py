from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from typing import Any, Dict
import json

def hello_world(request: HttpRequest, *args: any, **kwargs: any) -> JsonResponse:
    data: Dict[str, str] = {"message": "This is the message!"}
    return JsonResponse(data=data)

def echo(request: HttpRequest, *args: any, **kwargs: any) -> JsonResponse:
    body = request.body
    data: Dict[str, str] = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)