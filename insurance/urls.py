from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register('CarInsur' , views.CarInsurViewset)
router.register('CashSafeKeepInsura' , views.CashSafeKeepInsuraViewset)
router.register('CashTransferInsura' , views.CashTransferInsuraViewset)
router.register('TransportationInsur' , views.TransportationInsurViewset)
router.register('HonestyGuaranteeInsur' , views.HonestyGuaranteeInsurViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
    #viewset
    path('alandlus/', include(router.urls))
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]