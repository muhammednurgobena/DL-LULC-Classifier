from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('model_info/', views.model_info, name='model_info'),
    path('notebook/', views.notebook_view, name='notebook'),  # Correctly reference notebook_view
]