
from django.db import models

class Customer(models.Model):
    tenure = models.FloatField(default=1)
    monthly_charges = models.FloatField(default=70)
    total_charges = models.FloatField(default=70)
    
    dependents_yes = models.BooleanField(default=False)
    internetservice_fiber_optic = models.BooleanField(default=False)
    internetservice_no = models.BooleanField(default=False)
    
    onlinesecurity_no = models.BooleanField(default=False)
    onlinesecurity_no_internet_service = models.BooleanField(default=False)
    
    onlinebackup_no = models.BooleanField(default=False)
    onlinebackup_no_internet_service = models.BooleanField(default=False)
    
    deviceprotection_no = models.BooleanField(default=False)
    deviceprotection_no_internet_service = models.BooleanField(default=False)
    
    techsupport_no = models.BooleanField(default=False)
    techsupport_no_internet_service = models.BooleanField(default=False)
    
    streamingtv_no_internet_service = models.BooleanField(default=False)
    streamingmovies_no_internet_service = models.BooleanField(default=False)
    
    contract_1_year = models.BooleanField(default=False)
    contract_2_year = models.BooleanField(default=False)
    contract_monthly = models.BooleanField(default=False)
    
    paperlessbilling_yes = models.BooleanField(default=False)
    paymentmethod_electronic_check = models.BooleanField(default=False)
    
    prediction = models.BooleanField(null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)

#    def __str__(self):
#        return f"Customer (ID: {self.id})"
