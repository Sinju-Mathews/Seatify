from django.shortcuts import render,redirect
import firebase_admin
from datetime import datetime
from firebase_admin import storage, auth, firestore, credentials
import pyrebase


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
# Create your views here.

def UserRegistration(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})
    
    data=[]
    if request.method=="POST":
        email = request.POST.get("txtemail")
        password = request.POST.get("txtpwd")

        try:
            user = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error :
            return render(request,"Guest/UserRegistration.html",{"msg":error})
        photo=request.FILES.get("filephoto")
        if photo:
            path="user_photo/"+photo.name
            sd.child(path).put(photo)
            d_url=sd.child(path).get_url(None)

        data={"user_name": request.POST.get('txtname'),"user_gender": request.POST.get('gender'),
        "user_contact": request.POST.get('txtcontact'),"user_email": request.POST.get('txtemail'),
        "user_dob": request.POST.get('txtdob'),"user_address": request.POST.get('txtaddress'),
        "place_id": request.POST.get('ddlplace'),"user_photo": d_url,"user_id" : user.uid}
        db.collection("tbl_user").add(data)
        return render(request,"Guest/UserRegistration.html")
    else:
        return render(request,"Guest/UserRegistration.html",{"state":stlist})
    

def BusRegistration(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})
    
    data=[]
    if request.method=="POST":
        email = request.POST.get("txtemail")
        password = request.POST.get("txtpwd")

        try:
            user = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error :
            return render(request,"Guest/BusServiceRegistration.html",{"msg":error})
        logo=request.FILES.get("filelogo")
        proof=request.FILES.get("fileproof")
        if logo:
            path="bus_logo/"+logo.name
            sd.child(path).put(logo)
            l_url=sd.child(path).get_url(None)
        if proof:
            path="bus_proof/"+proof.name
            sd.child(path).put(logo)
            p_url=sd.child(path).get_url(None)
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

        data={"bs_name": request.POST.get('txtname'),"bs_contact": request.POST.get('txtcontact'),"bs_email": request.POST.get('txtemail'),"bs_doj": formatted_date,
        "bs_address": request.POST.get('txtaddress'),"place_id": request.POST.get('ddlplace'),"bs_logo": l_url,"bs_proof": p_url,"bs_status":0, "bs_id": user.uid}
        db.collection("tbl_bus_service").add(data)
        return render(request,"Guest/BusServiceRegistration.html")
    else:
        return render(request,"Guest/BusServiceRegistration.html",{"state":stlist})

def AjaxDistrict(request):
    dis = db.collection("tbl_district").where("state_id", "==", request.GET.get("sid")).stream()
    dis_data = []
    for d in dis:
        dis_data.append({"district":d.to_dict(),"id":d.id})
    return render(request,"Guest/AjaxDistrict.html",{"district":dis_data})

def AjaxPlace(request):
    pl = db.collection("tbl_place").where("district_id", "==", request.GET.get("did")).stream()
    pl_data = []
    for p in pl:
        pl_data.append({"place":p.to_dict(),"id":p.id})
    return render(request,"Guest/AjaxPlace.html",{"place":pl_data})

def Login(request):
    userid =adminid =busid = ""
    if request.method == "POST":
        email = request.POST.get("txtsname")
        password = request.POST.get("txtpwd")
        try:
            data = authe.sign_in_with_email_and_password(email,password)
        except:
            return render(request,"Guest/Login.html",{"msg":"Email and Password Error"})

        ids = data["localId"]
        user = db.collection("tbl_user").where("user_id", "==", ids).stream()
        for u in user:
            userid = u.id
            
        admin = db.collection("tbl_admin").where("admin_id", "==", ids).stream()
        for a in admin:
            adminid = a.id

        bus = db.collection("tbl_bus_service").where("bs_id", "==", ids).stream()
        for b in bus:
            busid = b.id

        if userid:
            request.session["uid"] = userid
            return redirect("webuser:homepage")
        elif adminid:
            request.session["aid"] = adminid
            return redirect("webAdmin:homepage")
        elif busid:
            request.session["bid"] = busid
            return redirect("webBusService:homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Error"})
        return render(request,"Guest/Login.html")
    else:
        return render(request,"Guest/Login.html")