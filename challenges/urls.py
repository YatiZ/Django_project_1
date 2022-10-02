from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name= "index"),
    path("<int:month>",views.number_month),
    path("<str:month>",views.string_month, name= "month-challenge"),
    
]