from django.urls import path
from django.conf.urls import *
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('bikes/',views.bikespage,name='bikes'),
    path('book/',views.book, name='book'),
    path(r'^status/1',views.book_process),
    path(r'^return_status/1',views.return_process),
    path('cart/',views.cart)
]
