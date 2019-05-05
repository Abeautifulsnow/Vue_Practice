from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

from .models import Books

# Create your views here.

@csrf_exempt
def create(request):
    print("create")
    obj = json.loads(request.body)
    name = obj['name']
    price = obj['price']
    try:
        book = Books(book_name=name, book_price=price, book_time=timezone.now())
        book.save()
        res = {
            "code": 200,
        }
    except Exception as e:
        res = {
            "code": 0,
            'errMsg': e,
        }
    return HttpResponse(json.dumps(res), content_type='application/json')

@csrf_exempt
def read(request):
    print("read")
    try:
        res = {
            "code": 200,
            "data": serializers.serialize("json", Books.objects.filter()),
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e,
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def update(request):
    print("update")
    obj = json.loads(request.body)
    pid = obj['id']
    name = obj['name']
    price = obj['price']
    try:
        Books.objects.filter(id=pid).update(book_price=price, book_name=name)
        res = {
            "code": 200,
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e,
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def delete(request):
    print("delete")
    obj = json.loads(request.body)
    print(obj)
    pid = obj['id']
    try:
        Books.objects.filter(id=pid).delete()
        res = {
            "code": 200,
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e,
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def search(request):
    print("search")
    content = request.GET['content']
    try:
        books = serializers.serialize("json", Books.objects.filter(book_name__contains=content))
        res = {
            "code": 200,
            "data": books,
        }
        print(books)
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e,
        }
    return HttpResponse(json.dumps(res), content_type="application/json")
