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

  path('setprice/',views.setprice,name="setprice"),

  path('bspverification/',views.bspverification,name="bspverification"),
  path('bs_accept/<str:id>',views.bs_accept,name="bs_accept"),
  path('bs_reject/<str:id>',views.bs_reject,name="bs_reject"),
  path('bs_viewmore/<str:id>',views.bs_viewmore,name="bs_viewmore"),
    
  path('viewcomplaints/',views.viewcomplaints,name="viewcomplaints"),
  path('replycomplaints/<str:id>',views.replycomplaints,name="replycomplaints"),

  path('viewfeedbacks/',views.viewfeedbacks,name="viewfeedbacks"),
  path('dataentry/',views.dataEntry,name="dataentry"),
]


    
