from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response
from LearnAPI.permissions import IsOwnerOrReadOnly

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        try:
            return Notification.objects.filter(user=self.request.user).order_by('-timestamp')
        except Exception as e:
            #print(f"Error fetching notifications: {e}")
            return Notification.objects.none()

class NotificationDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def delete(self, request, mid, *args, **kwargs):
        try:
            queryset = Notification.objects.filter(id=mid, user=self.request.user)
            if queryset.exists():
                queryset.delete()
                return Response({"message": "Notification deleted successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)