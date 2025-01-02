from django.shortcuts import render
from django.http import JsonResponse
from .forms import CustomerForm
import pandas as pd
import pickle
import logging
from .utils import load_model_components, preprocess_inputs, get_prediction_output

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load model components
model, scaler, model_features, numeric_fields = load_model_components()

def load_page(request):
    """
    Render the main form page.
    """
    form = CustomerForm()
    return render(request, 'home.html', {'form': form})


def about(request):
    """
    Render the about page.
    """
    return render(request, 'about.html')


def predict(request):
    """
    Handle form submission, process inputs, and return prediction results.
    """
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                # Preprocess form data into feature array
                features = preprocess_inputs(form.cleaned_data)

                # Create DataFrame with model's feature names
                input_df = pd.DataFrame([features], columns=model_features)

                # Scale numeric fields
                input_df[numeric_fields] = scaler.transform(input_df[numeric_fields])

                # Ensure compatibility with model's feature names
                input_df = input_df[model.feature_names_in_]

                # Log the reordered input DataFrame
                logger.debug(f"Reordered input DataFrame: {input_df.to_string(index=False)}")

                # Make prediction
                prediction = model.predict(input_df)[0]
                confidence = model.predict_proba(input_df)[0].max()

                # Get formatted output
                output1, output2 = get_prediction_output(prediction, confidence)

            except Exception as e:
                output1 = "Error processing the request"
                output2 = str(e)
                logger.error(f"Error: {e}")

            return render(request, 'home.html', {'form': form, 'output1': output1, 'output2': output2})
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = CustomerForm()
        return render(request, 'home.html', {'form': form})
