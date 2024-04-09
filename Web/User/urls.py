from django.urls import path
from User import views
app_name = "webuser"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('search/',views.search,name="search"),
    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),
    path('booking/<int:price>/<str:sid>/<str:from_stop>/<str:to_stop>/<str:arrive>/<str:depart>/', views.booking, name='booking'),
    path('confirmbooking/<str:id>/<int:total>/',views.confirmbooking,name="confirmbooking"),
    path('payment/<str:id>/',views.payment,name="payment"),
    path('mybookings/',views.mybookings,name="mybookings"),
    path('eachbooking/<str:id>/',views.eachbooking,name="eachbooking"),
    path('cancelbooking/<str:id>/',views.cancelbooking,name="cancelbooking"),
    path('usercomplaint/',views.usercomplaint,name="usercomplaint"),
    path('userfeedback/',views.userfeedback,name="userfeedback"),
]