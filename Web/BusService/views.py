
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
    bus = db.collection("tbl_bus_service").document(request.session["bid"]).get().to_dict()
    return render(request,"BusService/HomePage.html",{"bus":bus})   
    
def myprofile(request):
    bus = db.collection("tbl_bus_service").document(request.session["bid"]).get().to_dict()
    placelist=[]
    place = db.collection("tbl_place").document(bus["place_id"]).get().to_dict()
    district=db.collection("tbl_district").document(place["district_id"]).get().to_dict()
    state=db.collection("tbl_state").document(district["state_id"]).get().to_dict()
    placelist.append({"place":place,"district":district,"state":state}) 
    return render(request,"BusService/MyProfile.html",{"bus":bus,"pdata":placelist}) 

def editprofile(request):
    bus = db.collection("tbl_bus_service").document(request.session["bid"]).get().to_dict()
    placelist=[]
    place = db.collection("tbl_place").document(bus["place_id"]).get().to_dict()
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
            path="bus_logo/"+photo.name
            sd.child(path).put(photo)
            l_url=sd.child(path).get_url(None)
            db.collection("tbl_bus_service").document(request.session["bid"]).update({"bs_logo": l_url})

        db.collection("tbl_bus_service").document(request.session["bid"]).update({"bs_name": request.POST.get('txtname'),
        "bs_contact": request.POST.get('txtcontact'),
        "bs_address": request.POST.get('txtaddress'),
         "place_id": request.POST.get('ddlplace'),})
        return redirect("webBusService:myprofile")
    else:
        return render(request,"BusService/EditProfile.html",{"bus":bus,"pdata":placelist,"sdata":stlist})

def changepassword(request):
    user = db.collection("tbl_bus_service").document(request.session["bid"]).get().to_dict()
    email = user["bs_email"]
    # print(email)
    em_link = firebase_admin.auth.generate_password_reset_link(email)
    send_mail('Reset your password ', #subject
            "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + em_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your Seatify team.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
    return redirect("webBusService:myprofile")

def Schedule(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})

    rtdata=db.collection("tbl_route").stream()
    rtlist=[]
    for i in rtdata:
        route=i.to_dict()
        rtlist.append({"r_data":route,"rid":i.id})

    sddata=db.collection("tbl_schedule").where("bus_service_id", "==", request.session["bid"]).stream()
    sdlist=[]
    for i in sddata:
        schedule=i.to_dict()
        route=db.collection("tbl_route").document(schedule["route_id"]).get().to_dict()
        sdlist.append({"sd_data":schedule,"sdid":i.id,"route":route})
    
    data=[]
    if request.method=="POST":
        data={"route_id": request.POST.get('ddlroute'),"bus_name": request.POST.get('txtbus'),"time_scheduled": request.POST.get('txttime'),
        "bus_service_id":request.session["bid"]}
        db.collection("tbl_schedule").add(data)
        return redirect("webBusService:schedule")
    else:
        return render(request,"BusService/Schedule.html",{"state":stlist,"route":rtlist,"schedule":sdlist})

def ajaxroute(request):
    route = db.collection("tbl_route").where("from_id", "==", request.GET.get("from")).where("to_id", "==", request.GET.get("to")).stream()
    route_data = []
    for i in route:
        route_data.append({"route":i.to_dict(),"id":i.id})
    return render(request,"Guest/AjaxRoute.html",{"route":route_data})

def bscomplaint(request):
    id=request.session["bid"]

    compdata=db.collection("tbl_complaints").where("bus_service_id", "==", request.session["bid"]).stream()
    complist=[]
    for i in compdata:
        comp=i.to_dict()
        complist.append({"comp_data":comp,"id":i.id})
        
    if request.method=="POST":
        data={"complaint_title":request.POST.get("txtctitle")
            ,"complaint_content":request.POST.get("txtccontent"),"bus_service_id":id,"user_id":0}
        db.collection("tbl_complaints").add(data)
        return redirect("webBusService:bscomplaint")
    else:
        return render(request,"BusService/BSComplaints.html",{"data":complist})