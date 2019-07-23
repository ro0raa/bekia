from django.urls import path
from . import views
app_name='adv'

urlpatterns = [
 path('new/',views.add_advertise,name='save_adv'),
 path('show/<adv_id>/',views.show_adv,name='show_adv'),

 path('edit/<adv_id>/',views.update_adv,name='update_adv'),
 path('savetype/<type>/',views.save_adv_type,name='savetype'),
 path('deleteadv/<id>/', views.delete_adv, name='deleteadv'),

]
