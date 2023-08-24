from .models import Sorov
from .serializers import *
from rest_framework.generics import ListCreateAPIView

class SorovApiView(ListCreateAPIView):
    queryset = Sorov.objects.all()
    serializer_class  = SorovSerializer

