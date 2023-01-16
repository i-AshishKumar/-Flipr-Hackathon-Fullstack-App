from django.db.models import *
from rest_framework import permissions, viewsets

from .models import *
from .serializers import *

listofserializers = {
                        'bse':BSEserializer, 
                        'nse':NSEserializer, 
                        'ashok':AshokSerializer, 
                        'cipla':CiplaSerializer, 
                        'eicher':EicherSerializer, 
                        'reliance':RelianceSerializer, 
                        'tata':TatasteelSerializer
                    }
                    
class NSEModelViewSet(viewsets.ModelViewSet):
    queryset = NSE.objects.all()
    serializer_class = listofserializers['nse']

class BSEModelViewSet(viewsets.ModelViewSet):
    queryset = BSE.objects.all()
    serializer_class = listofserializers['bse']


class AshokModelViewSet(viewsets.ModelViewSet):
    queryset = AshokLeyland.objects.all()
    serializer_class = listofserializers['ashok']

class CiplaModelViewSet(viewsets.ModelViewSet):
    queryset = Cipla.objects.all()
    serializer_class = listofserializers['cipla']

class EicherModelViewSet(viewsets.ModelViewSet):
    queryset = EicherMotors.objects.all()
    serializer_class = listofserializers['eicher']

class RelianceModelViewSet(viewsets.ModelViewSet):
    queryset = Reliance.objects.all()
    serializer_class = listofserializers['reliance']

class TataModelViewSet(viewsets.ModelViewSet):
    queryset = TataSteel.objects.all()
    serializer_class = listofserializers['tata']