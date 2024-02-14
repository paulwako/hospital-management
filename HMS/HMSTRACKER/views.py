from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def greetingPage(request):
    return render(request,'login.html')

def home(request):
    return render(request,'basictest.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1') 
        
       
        if password == password1:
            if username:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'username is already in use')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username,password=password)
                    user.save();
                    return redirect('login')
            else:
                messages.info(request,'username is required')
                return redirect('signup')                    
        else:
            messages.info(request,'password mismatch')
            return redirect('signup')
    else:
        return render(request,'signup.html')
            


def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'you have logged in sucessfully')
            return redirect('condition')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:   
         return render(request,'logindata.html')

def condition(request):
    if request.method =='POST':
        weight = request.POST['weight']
        bp = request.POST['bp']
        hiv = request.POST['hiv']
        if weight and bp:
            preliminaryData.objects.all()
            data = preliminaryData(weight=weight,bloodPressure=bp,hiv=hiv)
            data.save()
            return redirect('consultation')
        else:
            messages.info(request,'blood pressure and weight is required')
            return redirect('condition')
    else:
        return render(request,'basictest.html')
    
def consultation(request):
    if request.method == 'GET':
        consultationRoom = request.GET.get('room')
        recomendation = request.GET.get('physcician-recomendation')
        if consultationRoom and recomendation:
            Consultation.objects.all()
            data = Consultation(consultationRoom=consultationRoom,recomendation=recomendation)
            data.save()
            return redirect('lab')
        else:
            return render(request,'consultation.html')
    else:
        return render(request,'consultation.html')
    
def lab(request):
    if request.method == 'POST':
        patientID = request.POST['patient']
        result = request.POST['result']
        if result and patientID:
            return redirect('prescription')
        else: 
            return redirect('lab')
    else:
        return render(request,'laboratory.html')
    
def prescription(request):
    if request.method == 'GET':
        prescription = request.GET.get('prescription')
        testresults = request.GET.get('test-results')
        if prescription and testresults:
            MedicineRecommendations.objects.all()
            data=MedicineRecommendations(prescription=prescription)
            data.save()
            return redirect('pharmacy')
        else:
            return redirect('prescription')
    else:
        return render(request, 'prescription.html')
        
    
def pharmacy(request):
    if request.method =='GET':
        prescription = request.GET.get('prescription')
        availableMedicine = request.GET.get('availableMedicine')
        outOfStock = request.GET.get('outOfStock')
        if prescription:
            Prescrition.objects.all()
            data = Prescrition(availableMedicine=availableMedicine,outOfStock=outOfStock)
            data.save()
            return redirect('accounts')
        else:
            return render(request,'pharmacy.html')
    else:
        return render(request,'pharmacy.html')
        
        

def accounts(request):
    return render(request,'Accounts.html')

def logout(request):
    auth.logout(request)
    return redirect('/')