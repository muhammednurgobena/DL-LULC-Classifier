# DL-LULC-Classifier
LULC-CNN-DL is a deep learning project for Land Use and Land Cover (LULC) classification using Convolutional Neural Networks (CNNs). It features can support multiple models, easy integration with Django and HTMX as frontend. This tool is ideal for environmental monitoring and geospatial analysis.


## Installation
### Prerequisites
- Python 3.x
- Django 5
- TensorFlow/Keras
- Pillow
- NumPy
- Simple you can install the requirements.txt fil 

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/saf1zun/DL-LULC-Classifier.git
    cd LULC_Predictor
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application** by navigating to `http://127.0.0.1:8000/` in your web browser.

## Usage
Upload a satellite image, select a model, and view the LULC predictions.

## Customization
Add more models, or modify LULC classes in `utils.py`.

## Contributing
Contributions are welcome!

## License
This project is licensed under the MIT License.

## Acknowledgments
Thanks to the open-source community for the tools and libraries used in this project.
## 1. Sentinel-2 Satellite images RGB from EuroSAT Dataset-link https://www.kaggle.com/datasets/apollo2506/eurosat-dataset

## 2. https://github.com/fedlunur

## The model can be made advanced and the output trained model can be togled in django view to enable multipple model runing on the dashboard.

## This web app and the backen model is developed for educational purpose only unle tunned seriously 


# Demo
![LULC](https://github.com/user-attachments/assets/16c02e88-fd32-4f63-9806-71e6a80674a9)




