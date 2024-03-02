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

    if request.method == "POST":
        fslist =[]
        from_stop = request.POST.get("ddlplace1")
        to_stop = request.POST.get("ddlplace2")
        stop_from_query = db.collection("tbl_stop").where("stopname_id", "==", from_stop).stream()
        for sf in stop_from_query:
            fs = sf.to_dict()
            fslist.append({"f_id":fs["route_id"], "fstop_no":fs["stop_number"]}) 

        route_ids = [fs["f_id"] for fs in fslist]
        stops_query = db.collection("tbl_stop").where("route_id", "in", route_ids).stream()

        tolist=[]
        for s in stops_query:
            stops_data = s.to_dict()
            if stops_data["stopname_id"] == to_stop:
                tolist.append({"t_id":stops_data["route_id"], "tstop_no":stops_data["stop_number"]})

        final_routes = []
        for fr in fslist:
            for to in tolist:
                if to['t_id'] == fr['f_id'] and to['tstop_no'] > fr['fstop_no']:
                    final_routes.append(to)

        ids_set = set()
        for route in final_routes:
             ids_set.add(route["t_id"])
        ids = list(ids_set)

        schedlist = []
        for route_id in ids:
            schedule_q = db.collection("tbl_schedule").where("route_id", "==", route_id).stream()
            for doc in schedule_q:
                schedule= doc.to_dict() 
                route = db.collection("tbl_route").document(schedule["route_id"]).get().to_dict()
                schedlist.append({"route_data": route, "scid":doc.id, "sched_data": schedule})
        return render(request,"User/SearchBus.html", {"schedule":schedlist})

    else:
        return render(request,"User/SearchBus.html",{"state":stlist})

def booking(request,id):
    return render(request,"User/Booking.html")

def usercomplaint(request):
    id=request.session["uid"]

    compdata=db.collection("tbl_complaints").where("user_id", "==", request.session["uid"]).stream()
    complist=[]
    for i in compdata:
        comp=i.to_dict()
        complist.append({"comp_data":comp,"id":i.id})
        
    if request.method=="POST":
        data={"complaint_title":request.POST.get("txtctitle")
            ,"complaint_content":request.POST.get("txtccontent"),"user_id":id,"center_id":0}
        db.collection("tbl_complaints").add(data)
        return redirect("webuser:usercomplaint")
    else:
        return render(request,"User/UserComplaint.html",{"data":complist})
