from rest_framework import generics
from .models import Professional
from .serializers import ProfessionalSerializer

class ProfessionalListAPIView(generics.ListAPIView):
    """
    API endpoint that returns a list of all professionals.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer