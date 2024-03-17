from django.shortcuts import render, redirect
import datetime
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
    return render(request,"User/SearchBus.html",{"state":stlist})

def ajaxsearch(request):
    fslist =[]
    from_stop = request.GET.get("from")
    to_stop = request.GET.get("to")
    fromplace = db.collection("tbl_place").document(from_stop).get().to_dict()
    fplace=fromplace["place_name"]
    toplace = db.collection("tbl_place").document(to_stop).get().to_dict()
    tplace=toplace["place_name"]
    stop_from_query = db.collection("tbl_stop").where("stopname_id", "==", from_stop).stream()
    for sf in stop_from_query:
        fs = sf.to_dict()
        fslist.append({"f_id":fs["route_id"], "fstop_no":fs["stop_number"], "fstop_dis":fs["stop_distance"], "fstime": fs["stop_time"]}) 

    route_ids = [fs["f_id"] for fs in fslist]
    stops_query = db.collection("tbl_stop").where("route_id", "in", route_ids).stream()

    tolist=[]
    for st in stops_query:
        stops_data = st.to_dict()
        if stops_data["stopname_id"] == to_stop:
            tolist.append({"t_id":stops_data["route_id"], "tstop_no":stops_data["stop_number"], "tstop_dis":stops_data["stop_distance"], "tstime": stops_data["stop_time"]})

    details_set = set()
    for fr in fslist:
        for to in tolist:
            if to['t_id'] == fr['f_id'] and to['tstop_no'] > fr['fstop_no']:
                details_tuple = (fr['f_id'], int(to["tstop_dis"]) - int(fr["fstop_dis"]), int(to["tstime"]), int(fr["fstime"]))
                details_set.add(details_tuple)
    details = list(details_set)
 
    docs=db.collection("tbl_price").order_by("date_added", direction=firestore.Query.DESCENDING).limit(1).get()
    for doc in docs:
        pr=doc.to_dict()
        price=pr["price"]
   
    schedlist = []
    for det in details:
        if request.GET.get("date")!="":
            schedule_q = db.collection("tbl_schedule").where("route_id", "==", det[0]).where("date_scheduled", "==", request.GET.get("date")).stream()
        else:
            current_date = datetime.datetime.now()
            formatted_date = current_date.strftime("%Y-%m-%d")
            schedule_q = db.collection("tbl_schedule").where("route_id", "==", det[0]).where("date_scheduled", ">=", formatted_date).stream()  
        for doc in schedule_q:
            schedule= doc.to_dict() 
            route = db.collection("tbl_route").document(schedule["route_id"]).get().to_dict()
            scheduled_time = datetime.datetime.strptime(schedule["time_scheduled"], "%H:%M")
            updated_time1 = scheduled_time + datetime.timedelta(minutes=det[3])
            updated_time2 = scheduled_time + datetime.timedelta(minutes=det[2])
            dtime = updated_time1.strftime("%H:%M")
            atime = updated_time2.strftime("%H:%M")
            tp=(int(det[1])*int(price))
            schedlist.append({"route_data": route, "scid":doc.id, "sched_data": schedule, "distance": det[1], "depart":dtime, "arrive":atime, "price":tp}  )       
    return render(request, "Guest/AjaxSearch.html", {"schedule": schedlist, "fplace": fplace, "tplace": tplace})
    


def booking(request,id):
    seatcount = 40
    seat_count = [2,7,12,17,22,27,32,37]
    seats_range = range(1, seatcount + 1)
    booked_seats = []
    bookedlist=[]
    booked_data = db.collection("tbl_booking").where("schedule_id", "==", id).where("booking_status", "==", 1).stream()
    for i in booked_data:     
        bookedlist.append(i.id)
    for b in bookedlist:
        seats_data= db.collection("tbl_seat").where("booking_id", "==", b).where("seat_status", "==", 0).stream()   
        for i in seats_data:
            seat=i.to_dict()
            print(seat)
            booked_seats.append(int(seat["seat_no"]))
    print(booked_seats)

    if request.method == "POST":
        selected_seats = []
        selected_seats = request.POST.getlist('txtcheck[]')
        print(selected_seats) 
        current_date = datetime.datetime.now()
        book_data={"schedule_id": id,"user_id":request.session["uid"],"booking_amount": "","booking_status":0 ,
        "booking_timepstamp":current_date}
        db.collection("tbl_booking").add(book_data)

        book_data = db.collection("tbl_booking").where("schedule_id", "==", id).where("booking_status", "==", 0)
        .where("user_id" ,"==", request.session["uid"])
        .order_by("booking_timepstamp", direction=firestore.Query.DESCENDING)
        .limit(1).stream()
        for i in book_data:     
            bookid=i.id
        for i in selected_seats:
            seat_data={"booking_id":bookid,"seat_no":i,"seat_status":0 }
            db.collection("tbl_seat").add(seat_data)
        return render(request, 'User/ConfirmBooking.html')
    else:     
        return render(request, 'User/Booking.html', {'seats_range': seats_range,"seat_count":seat_count,'booked':booked_seats})

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

def userfeedback(request):
    id=request.session["uid"]
    if request.method=="POST":
        data={"feedback_content":request.POST.get("txtfcontent")
            ,"user_id":id,"bus_service_id":0,"feedback_time":datetime.now()}
        db.collection("tbl_feedbacks").add(data)
        return redirect("webuser:userfeedback")
    else:
        return render(request,"User/UserFeedback.html")