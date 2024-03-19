from django.shortcuts import render
from .models import UserAccount , CarInsur , CashSafeKeepInsura , CashTransferInsura , TransportationInsur , HonestyGuaranteeInsur , FireInsur , CargoTransportInsur , NotifyingContarctorsInsur
from .serializers import CarInsurSerializer , CashSafeKeepInsuraSerializer , CashTransferInsuraSerializer , TransportationInsurSerializer , HonestyGuaranteeInsurSerializer , FireInsurSerializer , CargoTransportInsurSerializer , NotifyingContarctorsInsurSerializer
from rest_framework import viewsets

def index(request):
    return render(request, 'index.html')

class CarInsurViewset(viewsets.ModelViewSet):
    queryset = CarInsur.objects.all()
    serializer_class = CarInsurSerializer
    
class CashSafeKeepInsuraViewset(viewsets.ModelViewSet):
    queryset = CashSafeKeepInsura.objects.all()
    serializer_class = CashSafeKeepInsuraSerializer
    
class CashTransferInsuraViewset(viewsets.ModelViewSet):
    queryset = CashTransferInsura.objects.all()
    serializer_class = CashTransferInsuraSerializer
    
class TransportationInsurViewset(viewsets.ModelViewSet):
    queryset = TransportationInsur.objects.all()
    serializer_class = TransportationInsurSerializer
    
class HonestyGuaranteeInsurViewset(viewsets.ModelViewSet):
    queryset = HonestyGuaranteeInsur.objects.all()
    serializer_class = HonestyGuaranteeInsurSerializer
    
class FireInsurViewset(viewsets.ModelViewSet):
    queryset = FireInsur.objects.all()
    serializer_class = FireInsurSerializer
    
class CargoTransportInsurViewset(viewsets.ModelViewSet):
    queryset = CargoTransportInsur.objects.all()
    serializer_class = CargoTransportInsurSerializer
    
class NotifyingContarctorsInsurViewset(viewsets.ModelViewSet):
    queryset = NotifyingContarctorsInsur.objects.all()
    serializer_class = NotifyingContarctorsInsurSerializer