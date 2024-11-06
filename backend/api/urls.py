from django.urls import path
from .views import ProfessionalListAPIView, ProfessionalCreateAPIView, ProfessionalDestroyAPIView

urlpatterns = [
    path('professionals/', ProfessionalListAPIView.as_view(), name='professionals-list'),
    path('professionals/create/', ProfessionalCreateAPIView.as_view(), name='professionals-create'),
    path('professionals/delete/<int:pk>/', ProfessionalDestroyAPIView.as_view(), name='professionals-delete'),
]
