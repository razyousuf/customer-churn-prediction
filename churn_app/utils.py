import pickle
import pandas as pd
import logging
import os


# Configure logging
logger = logging.getLogger(__name__)

# Model and scaler loading function
def load_model_components():
    """
    Load pre-trained model, scaler, and model feature names.
    """
    try:
        # Load model, scaler, and feature names
        # Assuming the model files are in churn_app/models/ folder
        model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
        scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'scaler.pkl')
        
        # Load model and scaler
        model = pickle.load(open(model_path, 'rb'))
        scaler = pickle.load(open(scaler_path, 'rb'))

        model_features = [
            'tenure', 'monthlycharges', 'totalcharges', 'dependents_yes',
            'internetservice_fiber_optic', 'internetservice_no',
            'onlinesecurity_no', 'onlinesecurity_no_internet_service',
            'onlinebackup_no', 'onlinebackup_no_internet_service',
            'deviceprotection_no', 'deviceprotection_no_internet_service',
            'techsupport_no', 'techsupport_no_internet_service',
            'streamingtv_no_internet_service',
            'streamingmovies_no_internet_service', 'contract_1_year',
            'contract_2_year', 'contract_monthly', 'paperlessbilling_yes',
            'paymentmethod_electronic_check'
        ]
        numeric_fields = ['tenure', 'monthlycharges', 'totalcharges']
        
        logger.info("Model components loaded successfully.")
        return model, scaler, model_features, numeric_fields
    except Exception as e:
        logger.error(f"Error loading model components: {e}")
        raise e


# Preprocess the form data to match model input
def preprocess_inputs(form_data):
    """
    Preprocess the cleaned form data and return it in the correct order for the model.
    """
    try:
        # Extract numerical inputs
        tenure = form_data['tenure']
        monthlycharges = form_data['monthlycharges']
        totalcharges = form_data['totalcharges']

        # Extract and encode categorical inputs
        dependents_yes = 1 if form_data['dependents'] == '1' else 0
        #internet_service
        internetservice_fiber_optic = 1 if form_data['internetservice'] == 'fiber_optic' else 0
        internetservice_no = 1 if form_data['internetservice'] == 'no' else 0

        #online_security
        onlinesecurity_no = 1 if form_data['onlinesecurity'] == 'no' else 0
        onlinesecurity_no_internet_service = 1 if form_data['onlinesecurity'] == 'no_internet_service' else 0

        #online_backup
        onlinebackup_no = 1 if form_data['onlinebackup'] == 'no' else 0
        onlinebackup_no_internet_service = 1 if form_data['onlinebackup'] == 'no_internet_service' else 0

        #device_protection
        deviceprotection_no = 1 if form_data['deviceprotection'] == 'no' else 0
        deviceprotection_no_internet_service = 1 if form_data['deviceprotection'] == 'no_internet_service' else 0

        #tech_support
        techsupport_no = 1 if form_data['techsupport'] == 'no' else 0
        techsupport_no_internet_service = 1 if form_data['techsupport'] == 'no_internet_service' else 0

        #streaming_tv
        streamingtv_no_internet_service = 1 if form_data['streamingtv'] == 'no_internet_service' else 0

        #streaming_movies
        streamingmovies_no_internet_service = 1 if form_data['streamingmovies'] == 'no_internet_service' else 0

        #contract
        contract_1_year = 1 if form_data['contract'] == '1_year' else 0
        contract_2_year = 1 if form_data['contract'] == '2_year' else 0
        contract_monthly = 1 if form_data['contract'] == 'monthly' else 0

        paperlessbilling_yes = 1 if form_data['paperlessbilling'] == '1' else 0

        #payment_method 
        paymentmethod_electronic_check = 1 if form_data['paymentmethod'] == 'electronic_check' else 0

        # Assemble the feature array in the correct order
        features = [
            tenure, monthlycharges, totalcharges, dependents_yes,
            internetservice_fiber_optic, internetservice_no,
            onlinesecurity_no, onlinesecurity_no_internet_service,
            onlinebackup_no, onlinebackup_no_internet_service,
            deviceprotection_no, deviceprotection_no_internet_service,
            techsupport_no, techsupport_no_internet_service,
            streamingtv_no_internet_service, streamingmovies_no_internet_service,
            contract_1_year, contract_2_year, contract_monthly,
            paperlessbilling_yes, paymentmethod_electronic_check
        ]
        
        logger.info(f"Preprocessed inputs: {features}")
        return features
    except Exception as e:
        logger.error(f"Error preprocessing inputs: {e}")
        raise e


# Format the prediction output for display
def get_prediction_output(prediction, confidence):
    """
    Return a formatted output for the prediction.
    """
    try:
        if prediction == 1:
            output1 = "This customer is likely to churn!"
        else:
            output1 = "This customer is likely to continue!"
        
        output2 = f"Confidence: {confidence * 100:.2f}%"
        return output1, output2
    except Exception as e:
        logger.error(f"Error formatting prediction output: {e}")
        raise e
