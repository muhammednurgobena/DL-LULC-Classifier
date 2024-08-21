from django.shortcuts import render
from django.http import HttpResponse
from .utils import load_trained_model
import numpy as np
from django.core.files.storage import default_storage
from PIL import Image
import io

# Load the model once at the start
model = load_trained_model()

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')

        if uploaded_file:
            try:
                # Save uploaded file temporarily
                file_name = 'temp_image.jpg'
                file_path = default_storage.save(file_name, uploaded_file)
                
                # Open the saved file
                with default_storage.open(file_path) as f:
                    image = Image.open(f)
                    image = image.convert('RGB')  # Ensure the image is in RGB mode

                # Preprocess the image
                image = image.resize((64, 64))  # Adjust size as needed
                image_array = np.array(image) / 255.0  # Normalize if needed
                image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
                
                # Predict
                predictions = model.predict(image_array)
                
                # Map class indices to names
                class_names = {
                    0: 'Annual Crop',
                    1: 'Forest',
                    2: 'Herbaceous Vegetation',
                    3: 'Highway',
                    4: 'Industrial',
                    5: 'Pasture',
                    6: 'Permanent Crop',
                    7: 'Residential',
                    8: 'River',
                    9: 'Sea or Lake'
                }
                
                # Get the class probabilities
                probabilities = predictions[0]  # probabilities for each class
                
                # Sort classes by probability
                top_classes = np.argsort(probabilities)[::-1]  # Sort in descending order
                top_probabilities = probabilities[top_classes]
                
                # Prepare results for rendering
                top_results = [(class_names[idx], prob) for idx, prob in zip(top_classes, top_probabilities)]
                
                context = {
                    'top_results': top_results
                }
                
                return render(request, 'predictor/result.html', context)
            
            except Exception as e:
                print(f"Error during prediction: {e}")
                return HttpResponse(f"Error during prediction: {e}")
        
        return HttpResponse("No file uploaded.")

    return render(request, 'predictor/upload.html')

def model_info(request):
    return render(request, 'predictor/model_info.html')  # Render a template with model information

def notebook_view(request):
    return render(request, 'notebook.html')
