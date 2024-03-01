from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import storage, auth, firestore, credentials
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

db=firestore.client()
config = {
  "apiKey": "AIzaSyB_Dhe6Yx2w-9BgDKvoO9MA0rIvNF_DsNY",
  "authDomain": "mainproject-53373.firebaseapp.com",
  "projectId": "mainproject-53373",
  "storageBucket": "mainproject-53373.appspot.com",
  "messagingSenderId": "261253831557",
  "appId": "1:261253831557:web:7c9348c14950e4fe5102ec",
  "measurementId": "G-X8PCKYS6HC",
  "databaseURL":""
}

firebase=pyrebase.initialize_app(config)
sd=firebase.storage()
authe=firebase.auth()

def homepage(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    return render(request,"User/HomePage.html",{"user":user})   
    
def myprofile(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    placelist=[]
    place = db.collection("tbl_place").document(user["place_id"]).get().to_dict()
    district=db.collection("tbl_district").document(place["district_id"]).get().to_dict()
    state=db.collection("tbl_state").document(district["state_id"]).get().to_dict()
    placelist.append({"place":place,"district":district,"state":state}) 
    return render(request,"User/MyProfile.html",{"user":user,"pdata":placelist}) 

def editprofile(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    placelist=[]
    place = db.collection("tbl_place").document(user["place_id"]).get().to_dict()
    district=db.collection("tbl_district").document(place["district_id"]).get().to_dict()
    state=db.collection("tbl_state").document(district["state_id"]).get().to_dict()
    placelist.append({"place":place,"district":district,"state":state}) 

    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})

    if request.method=="POST":

        photo=request.FILES.get("photo_data")
        if photo:
            path="user_photo/"+photo.name
            sd.child(path).put(photo)
            d_url=sd.child(path).get_url(None)
            db.collection("tbl_user").document(request.session["uid"]).update({ "user_photo": d_url})

        db.collection("tbl_user").document(request.session["uid"]).update({"user_name": request.POST.get('txtname'),
        "user_gender": request.POST.get('gender'),"user_contact": request.POST.get('txtcontact'),
        "user_dob": request.POST.get('txtdob'),"user_address": request.POST.get('txtaddress'),
        "place_id": request.POST.get('ddlplace'),})
        return redirect("webuser:myprofile")
    else:
        return render(request,"User/EditProfile.html",{"user":user,"pdata":placelist,"sdata":stlist})

def changepassword(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    email = user["user_email"]
    # print(email)
    em_link = firebase_admin.auth.generate_password_reset_link(email)
    send_mail('Reset your password ', #subject
            "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + em_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your Seatify team.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
    return redirect("webuser:myprofile")

def search(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})

    # rtdata=db.collection("tbl_route").stream()
    # rtlist=[]
    # for i in rtdata:
    #     route=i.to_dict()

    # data=[]
    # if request.method=="POST":
    #     fromstop = db.collection("tbl_stop").where("stopname_id", "==", request.GET.get("ddlplace1")).get()
    #     tostop = db.collection("tbl_stop").where("stopname_id", "==", request.GET.get("ddlplace2")).get()
    #     stop=stop1+stop2
    #     stop_data = []
    #     for i in stop:
    #         stop_data.append({"stop":i.to_dict(),"id":i.id})
    #         print(stop_data)
    if request.method == "POST":
        fs_id = ts_id = route = ""
        from_stop = request.POST.get("ddlplace1")
        to_stop = request.POST.get("ddlplace2")
        stop_from = db.collection("tbl_stop").where("stopname_id", "==", from_stop).stream()
        for sf in stop_from:
            fs = sf.to_dict()
            fs_id = fs["route_id"]
        stop_to = db.collection("tbl_stop").where("stopname_id", "==", to_stop).stream()
        for sf in stop_to:
            fs = sf.to_dict()
            ts_id = fs["route_id"]
        if fs_id == ts_id:
            route = ts_id
        print(route)
        route_data = db.collection("tbl_route").document(route).get().to_dict()
        print(route_data)
        return render(request,"User/SearchBus.html",{"route":route_data})
    else:
        return render(request,"User/SearchBus.html",{"state":stlist})