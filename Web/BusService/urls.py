from django.urls import path
from BusService import views
app_name="webBusService"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('schedule/',views.Schedule,name="schedule"),
    path('ajaxroute/',views.ajaxroute,name="ajaxroute"),
    path('bscomplaint/',views.bscomplaint,name="bscomplaint"),
    path('bsfeedback/',views.bsfeedback,name="bsfeedback"),
]