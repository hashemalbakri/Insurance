from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserAccountManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))
        
    def create_user(self, first_name, last_name, email, password, **extra_fields):

        if not first_name:
            raise ValueError(_("Users must submit a first name"))
        
        if not last_name:
            raise ValueError(_("Users must submit a last name"))
        

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User: and email address is required"))
        
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save()

        return user
    
    def create_superuser(self, first_name, last_name, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        
        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin User: and email address is required"))
        

        user = self.create_user(first_name, last_name, email, password, **extra_fields)

        user.save()   

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name
    
    def __str__(self):
        return self.email
    
    
class CarInsur(models.Model):
    numberDoc = models.CharField(max_length= 150)
    nameInsured = models.CharField(max_length = 100)
    address = models.CharField(max_length= 200)
    coverType = models.CharField(max_length = 300)
    insurAmount = models.CharField(max_length = 500)
    insurFee = models.CharField(max_length = 400)
    insurPeriod = models.CharField(max_length = 300)
    carType = models.CharField(max_length = 200)
    manufactYear = models.CharField(max_length = 100)
    carColor = models.CharField(max_length = 100)
    carNumber = models.CharField(max_length =100)
    carInsurAmount = models.CharField(max_length = 200)
    civilResponsMaterial = models.CharField(max_length = 300)
    civilResponsPhysical = models.CharField(max_length = 300)
    wastedLossEveryAccident = models.CharField(max_length = 200)
    wastedLossTheft = models.CharField(max_length = 200)
    machineType = models.CharField(max_length = 200)
    vinNo = models.CharField(max_length = 200)
    netPremium = models.IntegerField()
    stampFees = models.IntegerField()
    diwanFees = models.IntegerField()
    adminFees = models.IntegerField()
    total = models.IntegerField()
    voucherNo = models.CharField(max_length = 600)
    voucherDate = models.CharField(max_length = 200)
    
    def __str__(self):
        return f"{self.nameInsured}"
    
class CashTransferInsura(models.Model):
    numberDoc = models.CharField(max_length= 150)
    releaseDate = models.CharField(max_length = 100)
    expiryDate = models.CharField(max_length = 100)
    nameInsured = models.CharField(max_length = 100)
    address = models.CharField(max_length= 200)
    idNo = models.CharField(max_length = 100)
    investLicenseNo = models.CharField(max_length = 200)
    phNo = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    valueInsurAmount = models.CharField(max_length = 200)
    currencyType = models.CharField(max_length = 100)
    amountWritten = models.CharField(max_length = 500)
    noMoveInsur = models.CharField(max_length = 300)
    valueMove = models.CharField(max_length = 100)
    moneyTrensferType = models.CharField(max_length = 200)
    moneyTrensferTypeDetails = models.TextField(max_length = 2000)
    transferMoneyFrom = models.CharField(max_length = 200)
    transferMoneyTo = models.CharField(max_length = 200)
    coverages = models.TextField(max_length = 5000)
    conditions = models.TextField(max_length = 5000)
    liabiltyLimited = models.TextField(max_length = 2000)
    wastedLoss = models.CharField(max_length = 200)
    netPremium = models.IntegerField()
    stampFees = models.IntegerField()
    diwanFees = models.IntegerField()
    adminFees = models.IntegerField()
    total = models.IntegerField()
    paymentMethod = (
        ('Cash','Cash'),
        ('Bank Transfer','Bank Transfer')
    )
    paymentReceiptNo = models.CharField(max_length = 200 ,null = True)
    transferNo = models.CharField(max_length = 200, null = True)
    transferDate = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return f"{self.email}"
    
class HonestyGuaranteeInsur(models.Model):
    numberDoc = models.CharField(max_length= 150)
    releaseDate = models.CharField(max_length = 100)
    expiryDate = models.CharField(max_length = 100)
    nameInsured = models.CharField(max_length = 100)
    address = models.CharField(max_length= 200)
    idNo = models.CharField(max_length = 100)
    investLicenseNo = models.CharField(max_length = 200)
    phNo = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    employeeName = models.CharField(max_length = 200)
    jobTitle = models.CharField(max_length = 300)
    workHours = models.CharField(max_length = 200)
    homeAddress = models.CharField(max_length = 300)
    idNumber = models.CharField(max_length = 400)
    compLiabilityLimit = models.TextField(max_length = 5000)
    conditions = models.TextField(max_length = 5000)
    wastedLoss = models.CharField(max_length = 200)
    netPremium = models.IntegerField()
    stampFees = models.IntegerField()
    diwanFees = models.IntegerField()
    adminFees = models.IntegerField()
    total = models.IntegerField()
    paymentMethod = (
        ('Cash','Cash'),
        ('Bank Transfer','Bank Transfer')
    )
    paymentReceiptNo = models.CharField(max_length = 200 ,null = True)
    transferNo = models.CharField(max_length = 200, null = True)
    transferDate = models.CharField(max_length = 200, null = True)
    
    def __str__(self):
        return f"{self.email}"
    
class CashSafeKeepInsura(models.Model):
    numberDoc = models.CharField(max_length= 150)
    releaseDate = models.CharField(max_length = 100)
    expiryDate = models.CharField(max_length = 100)
    nameInsured = models.CharField(max_length = 100)
    address = models.CharField(max_length= 200)
    idNo = models.CharField(max_length = 100)
    investLicenseNo = models.CharField(max_length = 200)
    phNo = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    valueInsurAmount = models.CharField(max_length = 200)
    currencyType = models.CharField(max_length = 100)
    amountWritten = models.CharField(max_length = 500)
    tanksType = models.CharField(max_length = 300)
    tanksNo = models.CharField(max_length = 200)
    depositedValue = models.CharField(max_length = 200)
    coverages = models.TextField(max_length = 5000)
    conditions = models.TextField(max_length = 5000)
    liabiltyLimited = models.TextField(max_length = 2000)
    wastedLoss = models.CharField(max_length = 200)
    netPremium = models.IntegerField()
    stampFees = models.IntegerField()
    diwanFees = models.IntegerField()
    adminFees = models.IntegerField()
    total = models.IntegerField()
    paymentMethod = (
        ('Cash','Cash'),
        ('Bank Transfer','Bank Transfer')
    )
    paymentReceiptNo = models.CharField(max_length = 200 ,null = True)
    transferNo = models.CharField(max_length = 200, null = True)
    transferDate = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return f"{self.email}"
    

class TransportationInsur(models.Model):
    numberDoc = models.CharField(max_length= 150)
    releaseDate = models.CharField(max_length = 100)
    nameInsured = models.CharField(max_length = 100)
    companyName = models.CharField(max_length = 200)
    address = models.CharField(max_length= 200)
    phNo = models.CharField(max_length = 100)
    
    beneficiaryName = models.CharField(max_length = 100)
    investLicenseNo = models.CharField(max_length = 200)
    address1 = models.CharField(max_length= 200)
    phNo = models.CharField(max_length = 100)
    contractCurr = (
        ('Dollar','Dollar'),
        ('IQ','IQ')
    )
    shipmentValue = models.CharField(max_length = 300)
    goodsInsurType = models.TextField(max_length = 5000)
    tripType = (
        ('Land','Land'),
        ('Sea','Sea'),
        ('Air','Air')
    )
    carNo = models.CharField(max_length = 100, null = True)
    shipName = models.CharField(max_length = 200,null = True)
    flightNo = models.CharField(max_length = 200 ,null = True)
    transportMethod = models.CharField(max_length = 200 ,null = True)
    shipmentDate = models.CharField(max_length = 200 ,null = True)
    roadTripFrom = models.CharField(max_length = 200 ,null = True)
    roadTripTo = models.CharField(max_length = 200 ,null = True)
    encapsulation = models.CharField(max_length = 200 ,null = True)
    coverageType = models.CharField(max_length = 200 ,null = True)
    addCoverage = models.CharField(max_length = 200 ,null = True)
    wastedLoss = models.CharField(max_length = 200)
    bankName = models.CharField(max_length = 200)
    licenseNo = models.CharField(max_length = 200)
    accreditationNo = models.CharField(max_length = 200)
    invoiceNo = models.CharField(max_length = 200)
    invoiceValue = models.CharField(max_length = 200)
    shipMethod = models.CharField(max_length = 200)
    totalInsurAmount = models.CharField(max_length = 200)
    conditions = models.TextField(max_length = 5000)
    netPremium = models.IntegerField()
    stampFees = models.IntegerField()
    diwanFees = models.IntegerField()
    adminFees = models.IntegerField()
    total = models.IntegerField()
    voucherNo = models.CharField(max_length = 200)
    voucherDate = models.CharField(max_length = 200)    
    
    def __str__(self):
        return f"{self.numberDoc}"
 

