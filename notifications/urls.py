from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet, NotificationDelete

router = DefaultRouter()
router.register(r'mynotifications', NotificationViewSet,
                basename='mynotification')
                

urlpatterns = [
    path('', include(router.urls)),
    path('notifications/delete/<int:mid>/', NotificationDelete.as_view()),
]
