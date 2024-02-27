from django.urls import path
from Guest import views
app_name="webGuest"
urlpatterns = [path('UserRegistration/',views.UserRegistration,name="UserRegistration"),
path('BusRegistration/',views.BusRegistration,name="BusRegistration"),
path('AjaxDistrict/',views.AjaxDistrict,name="AjaxDistrict"),
path('AjaxPlace/',views.AjaxPlace,name="AjaxPlace"),
path('Login/',views.Login,name="Login"),
    
]