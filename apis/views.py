from django.db.models import *
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

# def helper(inp):
#     #Cipla.objects.filter(date__range=["2023-01-11", "2023-01-12"]) --> 1 day Query 
#     #Cipla.objects.filter(date__range=["2023-01-07","2023-01-12"]) --> 5 days Query 
#     #Cipla.objects.filter(date__range=["2022-12-12", "2023-01-12"]) --> 1 month Query 
#     #Cipla.objects.filter(date__range=["2022-07-12", "2023-01-12"]) --> 6 month Query
#     #Cipla.objects.filter(date__range=["2022-01-12", "2023-01-12"]) --> 1 year Query 
#     #Cipla.objects.filter(date__range=["2018-01-15", "2023-01-12"]) --> 5 years Query 


#     day_open = inp.filter(date='2020-03-19').values()[0]['open']
#     day_high = inp.filter(date='2020-03-19').values()[0]['high']
#     day_low = inp.filter(date='2020-03-19').values()[0]['low']
    
#     one_year_high = inp.filter(date__range=["2022-01-12", "2023-01-12"]).aggregate(Max('high'))
#     one_year_low = inp.filter(date__range=["2022-01-12", "2023-01-12"]).aggregate(Min('low'))
    
#     five_year_high = inp.all().aggregate(Max('high'))
#     five_year_low = inp.all().aggregate(Min('low'))

#     return day_open,day_low,day_high, one_year_low, one_year_high, five_year_low, five_year_high
#     pass

listofserializers = {
                        'bse':BSEserializer, 
                        'nse':NSEserializer, 
                        'ashok':AshokSerializer, 
                        'cipla':CiplaSerializer, 
                        'eicher':EicherSerializer, 
                        'reliance':RelianceSerializer, 
                        'tata':TatasteelSerializer
                    }

# @api_view(['GET','POST'])

    # if request.method == 'GET':
    #     company = request.content
    #     obj = company.objects.all()
    #     serializer = listofserializers[company](obj,many=True)
    #     return Response(serializer.data)

    # day_open,day_low,day_high, one_year_low, one_year_high, five_year_low, five_year_high = helper(tmp)
    # d = {'day_open':day_open,'day_low':day_low,'day_high':day_high,'one_year_low':one_year_low,'one_year_high':one_year_high,'five_year_low':five_year_low,'five_year_high':five_year_high}

    # return Response(serializer.data)


class NSEModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = NSE.objects.all()
    serializer_class = listofserializers['nse']

class BSEModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BSE.objects.all()
    serializer_class = listofserializers['bse']


class AshokModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = AshokLeyland.objects.all()
    serializer_class = listofserializers['ashok']

class CiplaModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cipla.objects.all()
    serializer_class = listofserializers['cipla']

class EicherModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = EicherMotors.objects.all()
    serializer_class = listofserializers['eicher']

class RelianceModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reliance.objects.all()
    serializer_class = listofserializers['reliance']

class TataModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TataSteel.objects.all()
    serializer_class = listofserializers['tata']