from django.urls import path
from User import views
app_name = "webuser"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('search/',views.search,name="search"),
    path('booking/<str:id>',views.booking,name="booking"),
    path('usercomplaint/',views.usercomplaint,name="usercomplaint"),
    path('userfeedback/',views.userfeedback,name="userfeedback"),
]