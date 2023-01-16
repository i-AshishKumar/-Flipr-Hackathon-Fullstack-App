from django.urls import path,include
from .views import *
from rest_framework import routers
# from .api import UserAuthentication

router = routers.DefaultRouter()
router.register(r'bse', BSEModelViewSet)
router.register(r'nse', NSEModelViewSet)
router.register(r'ashok', AshokModelViewSet)
router.register(r'cipla', CiplaModelViewSet)
router.register(r'eicher', EicherModelViewSet)
router.register(r'reliance', RelianceModelViewSet)
router.register(r'tata', TataModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]