from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from crm.views import RegisterViewset, ClientViewset, ContractViewset, EventViewset

router = routers.SimpleRouter()
router.register('register', RegisterViewset, basename='register')
router.register('clients', ClientViewset, basename="clients")
router.register('contracts', ContractViewset, basename='contracts')
router.register('events', EventViewset, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]