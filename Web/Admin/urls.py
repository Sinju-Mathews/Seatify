from django.urls import path
from Admin import views

app_name="webAdmin"
urlpatterns = [
  path('State/',views.state,name="State"), 
  path('del_state/<str:id>',views.Del_state,name="del_state"),  
  path('edit_state/<str:id>',views.Edit_state,name="edit_state"),

  path('district/',views.District,name="district"), 
  path('del_dist/<str:id>',views.Del_dist,name="del_dist"), 
  path('edit_dist/<str:id>',views.Edit_dist,name="edit_dist"), 

  path('place/',views.Place,name="place"), 
  path('del_place/<str:id>',views.Del_place,name="del_place"), 

  path('AdminRegistration/',views.AdminRegistration,name="AdminRegistration"), 
  path('homepage/',views.homepage,name="homepage"),

  path('route/',views.Route,name="route"),
  path('del_route/<str:id>',views.Del_route,name="del_route"),

  path('stop/',views.Stop,name="stop"),
  path('del_stop/<str:id>',views.Del_stop,name="del_stop"),

  path('dataentry/',views.dataEntry,name="dataentry"),
]


    
