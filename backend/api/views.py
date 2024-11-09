from rest_framework import generics, status
from rest_framework.response import Response
from .models import Professional, Device
from .serializers import ProfessionalSerializer, DeviceSerializer


class ProfessionalListAPIView(generics.ListAPIView):
    """
    API endpoint that returns a list of all professionals.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalCreateAPIView(generics.CreateAPIView):
    """
    API endpoint that creates a new professional.
    """
    serializer_class = ProfessionalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProfessionalDestroyAPIView(generics.DestroyAPIView):
    """
    API endpoint that deletes a professional.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalRetrieveAPIView(generics.RetrieveAPIView):
    """
    API endpoint that retrieves a professional by id.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint that updates a professional.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class DeviceListAPIView(generics.ListAPIView):
    """
    API endpoint that returns a list of all devices.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceCreateAPIView(generics.CreateAPIView):
    """
    API endpoint that creates a new device.
    """
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeviceDestroyAPIView(generics.DestroyAPIView):
    """
    API endpoint that deletes a device.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceRetrieveAPIView(generics.RetrieveAPIView):
    """
    API endpoint that retrieves a device by id.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint that updates a device.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
