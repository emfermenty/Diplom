from django.urls import path
from .views import pdf_upload, pdf_list

urlpatterns = [
    path('pdf_upload/', pdf_upload, name='pdf_upload'),
    path('pdf_list/', pdf_list, name='pdf_list'),
]