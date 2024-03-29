from .models import UserAccount , CarInsur , CashSafeKeepInsura , CashTransferInsura , TransportationInsur , HonestyGuaranteeInsur , FireInsur , CargoTransportInsur , NotifyingContarctorsInsur
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        
class CarInsurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInsur
        fields = '__all__'
        
class CashSafeKeepInsuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashSafeKeepInsura
        fields = '__all__'
        
class CashTransferInsuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTransferInsura
        fields = '__all__'
        
class TransportationInsurSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationInsur
        fields = '__all__'
        
class HonestyGuaranteeInsurSerializer(serializers.ModelSerializer):
    class Meta:
        model = HonestyGuaranteeInsur
        fields = '__all__'

class FireInsurSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireInsur
        fields = '__all__'
        
class CargoTransportInsurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoTransportInsur
        fields = '__all__'
        
class NotifyingContarctorsInsurSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifyingContarctorsInsur
        fields = '__all__'
        
    
        
