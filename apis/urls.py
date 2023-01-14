from django.urls import path,include
from .views import *
from rest_framework import routers

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
]