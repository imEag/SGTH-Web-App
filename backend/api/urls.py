from django.urls import path
from .views import ProfessionalListAPIView, ProfessionalCreateAPIView, ProfessionalDestroyAPIView, \
    ProfessionalRetrieveAPIView, ProfessionalUpdateAPIView

urlpatterns = [
    path('professionals/', ProfessionalListAPIView.as_view(), name='professionals-list'),
    path('professionals/create/', ProfessionalCreateAPIView.as_view(), name='professionals-create'),
    path('professionals/delete/<int:pk>/', ProfessionalDestroyAPIView.as_view(), name='professionals-delete'),
    path('professionals/<int:pk>/', ProfessionalRetrieveAPIView.as_view(), name='professionals-retrieve'),
    path('professionals/update/<int:pk>/', ProfessionalUpdateAPIView.as_view(), name='professionals-update'),
]
