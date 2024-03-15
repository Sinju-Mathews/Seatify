from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import storage, auth, firestore, credentials
import pyrebase

db=firestore.client()

# Create your views here.
def state(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})
    if request.method=="POST":
        data={"state_name": request.POST.get('txtsname')}
        db.collection("tbl_state").add(data)
        return redirect("webAdmin:State")
    else:
        return render(request,"Admin/State.html",{"data":stlist})

def Del_state(request,id):
    db.collection("tbl_state").document(id).delete()
    return redirect("webAdmin:State")

def Edit_state(request,id):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})

    state=db.collection("tbl_state").document(id).get().to_dict()
    if request.method=="POST":
        db.collection("tbl_state").document(id).update({"state_name": request.POST.get('txtsname')})
        return redirect("webAdmin:State")
    else:
        return render(request,"Admin/State.html",{"state":state,"data":stlist})


def District(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})

    disdata=db.collection("tbl_district").stream()
    dislist=[]
    for i in disdata:
        district=i.to_dict()
        state = db.collection("tbl_state").document(district["state_id"]).get().to_dict()
        dislist.append({"d_data":district,"did":i.id,"state":state})
        
    if request.method=="POST":
        data={"state_id":request.POST.get('ddlstate'),"district_name": request.POST.get('txtdname')}
        db.collection("tbl_district").add(data)
        return redirect("webAdmin:district")
    else:
        return render(request,"Admin/District.html",{"sdata":stlist,"ddata":dislist})

def Del_dist(request,id):
    db.collection("tbl_district").document(id).delete()
    return redirect("webAdmin:district")

def Edit_dist(request,id):

    disdata=db.collection("tbl_district").stream()
    dislist=[]
    for i in disdata:
        district=i.to_dict()
        displaystate = db.collection("tbl_state").document(district["state_id"]).get().to_dict()
        dislist.append({"d_data":district,"did":i.id,"state":displaystate})

    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})
    district=db.collection("tbl_district").document(id).get().to_dict()
    state=db.collection("tbl_state").document(district["state_id"]).get().to_dict()

    if request.method=="POST":
        db.collection("tbl_district").document(id).update({"district_name": request.POST.get('txtdname'),"state_id":request.POST.get('ddlstate')})
        return redirect("webAdmin:district")
    else:
        return render(request,"Admin/District.html",{"sdata":stlist, "state":state, "district":district,"ddata":dislist})

def Place(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})
        
    placedata=db.collection("tbl_place").stream()
    placelist=[]
    for i in placedata:
        place=i.to_dict()
        district=db.collection("tbl_district").document(place["district_id"]).get().to_dict()
        state=db.collection("tbl_state").document(district["state_id"]).get().to_dict()
        placelist.append({"p_data":place,"pid":i.id,"district":district,"state":state})
        
    if request.method=="POST":
        data={"district_id":request.POST.get('ddldist'),"place_name": request.POST.get('txtpname')}
        db.collection("tbl_place").add(data)
        return redirect("webAdmin:place")
    else:
        return render(request,"Admin/Place.html",{"sdata":stlist,"pdata":placelist})

def Del_place(request,id):
    db.collection("tbl_place").document(id).delete()
    return redirect("webAdmin:place")

def AdminRegistration(request):
    data=[]
    if request.method=="POST":
        email = request.POST.get("txtemail")
        password = request.POST.get("txtpwd")

        try:
            user = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error :
            return render(request,"Admin/AdminRegistration.html",{"msg":error})

        data={"admin_name": request.POST.get('txtname'),"admin_contact": request.POST.get('txtcontact'),"admin_email": request.POST.get('txtemail'),"admin_id" : user.uid}
        db.collection("tbl_admin").add(data)
        return render(request,"Admin/AdminRegistration.html")
    else:
        return render(request,"Admin/AdminRegistration.html")

def homepage(request):
    admin = db.collection("tbl_admin").document(request.session["aid"]).get().to_dict()
    return render(request,"Admin/AdminHome.html",{"admin":admin})

def Route(request):
    stdata=db.collection("tbl_state").stream()
    stlist=[]
    for i in stdata:
        state=i.to_dict()
        stlist.append({"s_data":state,"sid":i.id})

    routedata=db.collection("tbl_route").stream()
    routelist=[]
    for i in routedata:
        route=i.to_dict()
        frompl=db.collection("tbl_place").document(route["from_id"]).get().to_dict()
        topl=db.collection("tbl_place").document(route["to_id"]).get().to_dict()
        routelist.append({"rout_data":route,"rid":i.id,"from":frompl,"to":topl})
    
    data=[]
    if request.method=="POST":
        data={"route_name": request.POST.get('txtroute'),"from_id": request.POST.get('ddlplace1'),"to_id": request.POST.get('ddlplace2'),"time_taken": request.POST.get('txttime'),
        "distance": request.POST.get('txtkm')}
        db.collection("tbl_route").add(data)
        return redirect("webAdmin:route")
    else:
        return render(request,"Admin/Route.html",{"state":stlist,"route":routelist})

def Del_route(request,id):
    db.collection("tbl_route").document(id).delete()
    return redirect("webAdmin:route")


def Stop(request):
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

    stopdata=db.collection("tbl_stop").stream()
    stoplist=[]
    for i in stopdata:
        stop=i.to_dict()
        stpname=db.collection("tbl_place").document(stop["stopname_id"]).get().to_dict()
        route=db.collection("tbl_route").document(stop["route_id"]).get().to_dict()
        stoplist.append({"stop_data":stop,"stid":i.id,"stopname":stpname,"route":route})
    
    data=[]
    if request.method=="POST":
        data={"route_id": request.POST.get('ddlroute'),"stopname_id": request.POST.get('ddlplace1'),"stop_number": request.POST.get('stopno'),"stop_time": request.POST.get('timestop'),
        "stop_distance": request.POST.get('kmstop')}
        db.collection("tbl_stop").add(data)
        return redirect("webAdmin:stop")
    else:
        return render(request,"Admin/Stop.html",{"state":stlist,"route":rtlist,"stop":stoplist})
    
def Del_stop(request,id):
    db.collection("tbl_stop").document(id).delete()
    return redirect("webAdmin:stop")

def bspverification(request):
    bspdata=db.collection("tbl_bus_service").where("bs_status", "==", 0).stream()
    bsplist=[]
    for i in bspdata:
        bs=i.to_dict()
        bsplist.append({"bs_data":bs,"id":i.id})
        
    bspdata=db.collection("tbl_bus_service").where("bs_status", "==", 1).stream()
    bsplist2=[]
    for i in bspdata:
        bs=i.to_dict()
        bsplist2.append({"bs_data":bs,"aid":i.id})

    bspdata=db.collection("tbl_bus_service").where("bs_status", "==", 2).stream()
    bsplist3=[]
    for i in bspdata:
        bs=i.to_dict()
        bsplist3.append({"bs_data":bs,"rid":i.id})
    
    return render(request,"Admin/BSPVerification.html",{'data':bsplist,"data2":bsplist2,"data3":bsplist3})

def bs_accept(request,id):
    db.collection("tbl_bus_service").document(id).update({"bs_status":1})
    return redirect("webAdmin:bspverification")

def bs_reject(request,id):
    db.collection("tbl_bus_service").document(id).update({"bs_status":2})
    return redirect("webAdmin:bspverification")

def bs_viewmore(request,id):
    bs = db.collection("tbl_bus_service").document(id).get().to_dict()
    place=db.collection("tbl_place").document(bs["place_id"]).get().to_dict()
    district=db.collection("tbl_district").document(place["district_id"]).get().to_dict()
    state=db.collection("tbl_state").document(district["state_id"]).get().to_dict()
    return render( request,"Admin/BSViewMore.html",{ "bs":bs ,"place":place,"district":district,"state":state} )

def viewcomplaints(request):
    ccompdata=db.collection("tbl_complaints").where("bus_service_id","!=",0).stream()
    ccomplist=[]
    for i in ccompdata:
        comp=i.to_dict()
        busservice=db.collection("tbl_bus_service").document(comp["bus_service_id"]).get().to_dict()
        ccomplist.append({"ccomp_data":comp,"id":i.id,"busservice":busservice})

    ccompdata=db.collection("tbl_complaints").where("user_id","!=",0).stream()
    ccomplist2=[]
    for i in ccompdata:
        comp=i.to_dict()
        user=db.collection("tbl_user").document(comp["user_id"]).get().to_dict()
        ccomplist2.append({"ccomp_data":comp,"id":i.id,"user":user})
    return render(request,"Admin/ViewComplaints.html",{"data":ccomplist,"data2":ccomplist2})

def replycomplaints(request,id):
    if request.method=="POST":
        db.collection("tbl_complaints").document(id).update({"complaint_reply":request.POST.get("txtreply")})
        return redirect("webAdmin:viewcomplaints")
    else:
        return render(request,"Admin/ReplyComplaints.html")

def viewfeedbacks(request):
    feeddata=db.collection("tbl_feedbacks").where("bus_service_id","!=",0).stream()
    feedlist1=[]
    for i in feeddata:
        feed=i.to_dict()
        bs=db.collection("tbl_bus_service").document(feed["bus_service_id"]).get().to_dict()
        feedlist1.append({"bfeed_data":feed,"id":i.id,"bs":bs})

    feeddata=db.collection("tbl_feedbacks").where("user_id","!=",0).stream()
    feedlist2=[]
    for i in feeddata:
        feed=i.to_dict()
        user=db.collection("tbl_user").document(feed["user_id"]).get().to_dict()
        feedlist2.append({"ufeed_data":feed,"id":i.id,"user":user})
    return render(request,"Admin/ViewFeedbacks.html",{"data":feedlist1,"data2":feedlist2})

def dataEntry(request):
    districts = [ 
    ] 
    state_id = ""
# Replace with actual state ID     9xFDoazuqviGXTvX01Je  AMqnUMYRLzQKbYp7361R
    for district in districts:
        data = {"state_id": state_id, "district_name": district}
        db.collection("tbl_district").add(data)
    return redirect("webAdmin:district")

