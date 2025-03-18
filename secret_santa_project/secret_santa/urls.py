from django.urls import path
from .views import upload_employees, generate_secret_santa, export_secret_santa

urlpatterns = [
    path('upload/', upload_employees, name='upload_employees'),
    path('generate/', generate_secret_santa, name='generate_secret_santa'),
    path('export/', export_secret_santa, name='export_secret_santa'),
]
