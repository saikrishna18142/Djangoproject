from django.urls import path
from .import views
urlpatterns=[
    path('',views.first),
   # path('vcube/',views.secondview),
    path('sai/',views.thirdview),
] 