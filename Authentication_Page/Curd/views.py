from django.shortcuts import render,redirect
from .models import Users   #users is a class name is defined in models.py 

# Create your views here.
def home(request):
    result=Users.objects.all()
    return render(request,"curd/home.html", {'result':result})

def add_user(request):
   if request.method=="POST":
      print("User Added")

      #curds_srnumber,urds_lname this all are variables we put other name also
      #retrive the user inputs
      curds_srnumber=request.POST.get("curd_srnumber")
      curds_fname=request.POST.get("curd_fname")
      curds_lname=request.POST.get("curd_lname")
      curds_email=request.POST.get("curd_email")
      curds_address=request.POST.get("curd_address")
      curds_phonenumber=request.POST.get("curd_phonenumber")

    #   #create an object for models

      x=Users()
      x.srnumber=curds_srnumber
      x.fname=curds_fname
      x.lname=curds_lname
      x.email=curds_email
      x.address=curds_address
      x.phonenumber=curds_phonenumber

      x.save()  # for save data
      return redirect("/Curd/")
   return render(request,"curd/add_user.html", {})
   
 # For Delete user  
def Delete_curd(request,srnumber):
      r=Users.objects.get(pk=srnumber)
      r.delete()
      return redirect("/Curd/")

# For Update User
def Update_curd(request,srnumber):
       r1=Users.objects.get(pk=srnumber)
    #    return redirect("/Curd/")
       return render(request,"curd/update_curd.html",{'r1':r1})
  
     

    

# Save updated data in Database
def do_Update_curd(request,srnumber):
    curds_srnumber=request.POST.get("curd_srnumber")
    curds_fname=request.POST.get("curd_fname")
    curds_lname=request.POST.get("curd_lname")
    curds_email=request.POST.get("curd_email")
    curds_address=request.POST.get("curd_address")
    curds_phonenumber=request.POST.get("curd_phonenumber")    

    y=Users.objects.get(pk=srnumber)
    y.srnumber=curds_srnumber
    y.fname=curds_fname
    y.lname=curds_lname
    y.email=curds_email
    y.address=curds_address
    y.phonenumber=curds_phonenumber
    y.save()
    return redirect("/Curd/")
     

