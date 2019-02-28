#!usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'dapeng'
__date__ = '19-2-26 下午10:13'
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('add_book', add_book),
    path('show_books', show_books),
]

app_name = 'myapp'
