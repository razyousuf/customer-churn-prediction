import pickle
import pandas as pd

# Load pre-trained components
model = pickle.load(open('churn_app/ml_models/model.pkl', 'rb'))
scaler = pickle.load(open('churn_app/ml_models/scaler.pkl', 'rb'))

# Feature names
model_features = [
    'tenure', 'monthlycharges', 'totalcharges', 'dependents_yes',
    'internetservice_fiber_optic', 'internetservice_no',
    'onlinesecurity_no', 'onlinesecurity_no_internet_service',
    'onlinebackup_no', 'onlinebackup_no_internet_service',
    'deviceprotection_no', 'deviceprotection_no_internet_service',
    'techsupport_no', 'techsupport_no_internet_service',
    'streamingtv_no_internet_service', 'streamingmovies_no_internet_service',
    'contract_1_year', 'contract_2_year', 'contract_monthly',
    'paperlessbilling_yes', 'paymentmethod_electronic_check'
]

numeric_fields = ['tenure', 'monthlycharges', 'totalcharges']
