from rest_framework import generics, status
from rest_framework.response import Response
from .models import Professional
from .serializers import ProfessionalSerializer


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
