from rest_framework import routers
from .api import BasicViewSet

router = routers.DefaultRouter()
router.register('api/basic', BasicViewSet, 'basic')

urlpatterns = router.urls
