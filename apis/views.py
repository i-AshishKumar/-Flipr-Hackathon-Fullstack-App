from django.db.models import *
from rest_framework import permissions, viewsets
from rest_framework.decorators import action

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
    allowed_methods = ["GET"]

class BSEModelViewSet(viewsets.ModelViewSet):
    queryset = BSE.objects.all()
    serializer_class = listofserializers['bse']
    allowed_methods = ["GET"]


class AshokModelViewSet(viewsets.ModelViewSet):
    queryset = AshokLeyland.objects.all()
    serializer_class = listofserializers['ashok']
    allowed_methods = ["GET"]

class CiplaModelViewSet(viewsets.ModelViewSet):
    queryset = Cipla.objects.all()
    serializer_class = listofserializers['cipla']
    allowed_methods = ["GET"]

class EicherModelViewSet(viewsets.ModelViewSet):
    queryset = EicherMotors.objects.all()
    serializer_class = listofserializers['eicher']
    allowed_methods = ["GET"]

class RelianceModelViewSet(viewsets.ModelViewSet):
    queryset = Reliance.objects.all()
    serializer_class = listofserializers['reliance']
    allowed_methods = ["GET"]

class TataModelViewSet(viewsets.ModelViewSet):
    queryset = TataSteel.objects.all()
    serializer_class = listofserializers['tata']
    allowed_methods = ["GET"]