from django.urls import path
from . import views

urlpatterns = [
 path('new/',views.add_advertise),

]
