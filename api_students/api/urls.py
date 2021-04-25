from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import StudentViewSet

v1_router = DefaultRouter()
v1_router.register('students', StudentViewSet, basename='Student')

urlpatterns = [
        path('v1/', include(v1_router.urls)),
        path('v1/token/', TokenObtainPairView.as_view(),
             name='token_obtain_pair'),
        path('v1/token/refresh/', TokenRefreshView.as_view(),
             name='token_refresh'),
]
