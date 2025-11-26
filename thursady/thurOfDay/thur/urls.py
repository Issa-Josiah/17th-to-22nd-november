from ensurepip import bootstrap

from django.urls import path
from . import views

urlpatterns = [
    path('thursday/', views.monday ),
    path('strap/', views.boot),

]
