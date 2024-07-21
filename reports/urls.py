
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet
from reports import views

router = DefaultRouter()
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
    path('comments/<int:pk>/reports/', ReportViewSet.as_view
         ({'get': 'comment_reports'}), name='comment-reports')
]
