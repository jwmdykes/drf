from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.forms.models import model_to_dict
from typing import Dict
import json

from products.models import Product

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

def random_product(request: HttpRequest, *args: any, **kwargs: any) -> HttpResponse:
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
    return JsonResponse(data)
