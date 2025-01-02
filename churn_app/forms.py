from django import forms

class CustomerForm(forms.Form):
    # Define fields for the customer form
    tenure = forms.IntegerField(label='Tenure (in months)', required=True, min_value=0, max_value=9999, initial=1)
    monthlycharges = forms.FloatField(label='Monthly Charges', required=True, min_value=0, max_value=9999, initial=70)
    totalcharges = forms.FloatField(label='Total Charges', required=True, min_value=0, max_value=9999, initial=70)
    
    dependents_choices = [
        ('1', '______________Yes_____________'),
        ('0', '______________No_____________')
    ]
    dependents = forms.ChoiceField(label='Dependents', choices=dependents_choices, required=True)
    
    internetservice_choices = [
        ('no', '______________No_____________'),
        ('fiber_optic', 'Fiber_Optic'),
        ('dsl', 'DSL'),
    ]
    internetservice = forms.ChoiceField(label='Internet Service', choices=internetservice_choices, required=True)
    
    onlinesecurity_choices = [
        ('yes', '______________Yes_____________'),
        ('no', '______________No_____________'),
        ('no_internet_service', 'No_Internet_Service')
    ]
    onlinesecurity = forms.ChoiceField(label='Online Security', choices=onlinesecurity_choices, required=True)
    
    onlinebackup_choices = [
        ('yes', '______________Yes_____________'),
        ('no', '______________No_____________'),
        ('no_internet_service', 'No_Internet_Service')
    ]
    onlinebackup = forms.ChoiceField(label='Online Backup', choices=onlinebackup_choices, required=True)
    
    deviceprotection_choices = [
        ('yes', '______________Yes_____________'),
        ('no', '______________No_____________'),
        ('no_internet_service', 'No_Internet_Service')
    ]
    deviceprotection = forms.ChoiceField(label='Device Protection', choices=deviceprotection_choices, required=True)
    
    techsupport_choices = [
        ('yes', '______________Yes_____________'),
        ('no', '______________No_____________'),
        ('no_internet_service', 'No_Internet_Service'),
    ]
    techsupport = forms.ChoiceField(label='Tech Support', choices=techsupport_choices, required=True)
    
    streamingtv_choices = [
        ('yes', '______________Yes_____________'),
        ('no_internet_service', 'No_Internet_Service')
    ]
    streamingtv = forms.ChoiceField(label='Streaming TV', choices=streamingtv_choices, required=True)
    
    streamingmovies_choices = [
        ('yes', '______________Yes_____________'),
        ('no_internet_service', 'No_Internet_Service')
    ]
    streamingmovies = forms.ChoiceField(label='Streaming Movies', choices=streamingmovies_choices, required=True)
    
    contract_choices = [
       ('1_year', 'One Year'),
        ('2_year', 'Tow Years'),
        ('monthly', 'Month-to-Month Contract')
    ]
    contract = forms.ChoiceField(label='Contract', choices=contract_choices, required=True)
    
    paperlessbilling_choices = [
        ('1', '______________Yes_____________'),
        ('0', '______________No_____________')
    ]
    paperlessbilling = forms.ChoiceField(label='Paperless Billing', choices=paperlessbilling_choices, required=True)
    
    paymentmethod_choices = [
        ('electronic_check', 'Electronic Check'),
        ('other', 'Other means of Payments')
        # ('bank_transfer', 'Bank Transfer'),
        # ('credit_card', 'Credit Card')
    ]
    paymentmethod = forms.ChoiceField(label='Payment Method', choices=paymentmethod_choices, required=True)
