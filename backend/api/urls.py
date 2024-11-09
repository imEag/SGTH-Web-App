from django.urls import path
from .views import ProfessionalListAPIView, ProfessionalCreateAPIView, ProfessionalDestroyAPIView, \
    ProfessionalRetrieveAPIView, ProfessionalUpdateAPIView, DeviceListAPIView, DeviceCreateAPIView, \
    DeviceDestroyAPIView, DeviceUpdateAPIView, DeviceRetrieveAPIView

urlpatterns = [
    path('professionals/', ProfessionalListAPIView.as_view(), name='professionals-list'),
    path('professionals/create/', ProfessionalCreateAPIView.as_view(), name='professionals-create'),
    path('professionals/delete/<int:pk>/', ProfessionalDestroyAPIView.as_view(), name='professionals-delete'),
    path('professionals/<int:pk>/', ProfessionalRetrieveAPIView.as_view(), name='professionals-retrieve'),
    path('professionals/update/<int:pk>/', ProfessionalUpdateAPIView.as_view(), name='professionals-update'),
    path('devices/', DeviceListAPIView.as_view(), name='devices-list'),
    path('devices/create/', DeviceCreateAPIView.as_view(), name='devices-create'),
    path('devices/delete/<int:pk>/', DeviceDestroyAPIView.as_view(), name='devices-delete'),
    path('devices/<int:pk>/', DeviceRetrieveAPIView.as_view(), name='devices-retrieve'),
    path('devices/update/<int:pk>/', DeviceUpdateAPIView.as_view(), name='devices-update')
]
