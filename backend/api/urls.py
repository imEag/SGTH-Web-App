from django.urls import path
from .views import ProfessionalListAPIView

urlpatterns = [
    path('professionals/', ProfessionalListAPIView.as_view(), name='professionals-list'),
]