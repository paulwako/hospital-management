from tkinter import CASCADE
from django.db import models

# Create your models here.
class preliminaryData(models.Model):
    weight = models.IntegerField()
    bloodPressure = models.IntegerField()
    hiv = models.CharField(max_length=10)
    
class Consultation(models.Model):
    consultationRoom = models.IntegerField()
    recomendation = models.TextField()
    
class Laboratory(models.Model):
    physcicianRoom = models.ForeignKey(Consultation,on_delete=callable)
    patientId = models.IntegerField()
    patientName = models.CharField(max_length=50)
    testResults = models.TextField()

class MedicineRecommendations(models.Model):
    prescription = models.TextField()
    
class Prescrition(models.Model):
    availableMedicine = models.TextField()
    outOfStock = models.TextField()
    

    
class Accounts(models.Model):
    paymentMode = models.CharField(max_length=100)
    TotalCost = models.DecimalField(decimal_places=3,default=0.000,max_digits=10)
    transactionID = models.CharField(max_length=15)
    paidAmount = models.DecimalField(decimal_places=3,default=0.000,max_digits=10)
    paymentDate = models.DateTimeField(auto_now_add=True)
    