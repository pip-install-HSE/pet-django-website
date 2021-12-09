from django.urls import path
from .views import *

urlpatterns = [
    path('filter/', filter_view, name='filter'),

    path('personal/', personal_view, name='personal'),

    path('result/', result, name='result'),
]