from django.shortcuts import render, redirect ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from managerdashboard.models import *
# from dashboard.user.models import *
from django.contrib.auth.decorators import login_required
import smtplib


# Create your views here.
@login_required
def managerpanel(req):

    bookings=Booking.objects.all()
    return render(req, 'managerpanel.html',{'bookings':bookings})


def managerlogin(req):
    if req.method == "POST":
        uname = req.POST['uname']
        password = req.POST['passwordmn']

        user=auth.authenticate(username=uname,password=password)
       
        if user is not None:
            if user.is_superuser:
                auth.login(req,user)
                return redirect('managerpanel')
            else:
                messages.info(req, "Email/Password Invalid!!")
                return redirect('managerlogin')
            
            
        else:
            messages.info(req, "Email/Password Invalid!!")
            return redirect('managerlogin')
        
    else:
        return render(req, 'index.html')



def logoutpanel(req):
    auth.logout(req)
    return redirect('managerlogin')

# def approve(req):

#     if req.method == "POST":
#         id = req.POST['approveid']
#         data = req.POST['approve']

#         email = req.POST['email']
#         name = req.POST['name']
#         vname = req.POST['vname']

#         approve=UserHistory.objects.get(id=id)
#         approve.Status = data
#         approve.save() 
#         messages.info(req, "Booking Approved!")

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login('psujata1974@gmail.com', 'yrre cfnt dxsa udcx')
#         server.sendmail('psujata1974@gmail.com', email ,'hi,' + name + 'your booking approved by '+ vname +'')
#         server.close()

#         return redirect('managerpanel')


#     else:
#         return HttpResponse("error 404 not found")



    
# def reject(req):

#     if req.method == "POST":
#         id = req.POST['rejectid']
#         data = req.POST['reject']

#         email = req.POST['email']
#         name = req.POST['name']
#         vname = req.POST['vname']

#         reject=UserHistory.objects.get(id=id)
#         reject.Status = data
#         reject.save() 
#         messages.info(req, "Booking Rejected!")

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login('psujata1974@gmail.com', 'yrre cfnt dxsa udcx')
#         server.sendmail('psujata1974@gmail.com', email ,'hi,' + name + 'your booking rejected by ' + vname +'')
#         server.close()

#         return redirect('managerpanel')
     

#     else:
#         return HttpResponse("error 404 not found")


    

def action(req):
    if req.method == "POST":
        myid = req.POST.get('id')
        book=Booking.objects.get(id=myid)
        print(book.status)
        book.status=req.POST.get('status')
        book.save()
    return redirect('managerpanel')

# def reject(req):
#     if req.method == "POST":
#         id = req.POST['approveid']