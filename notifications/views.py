from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            return Notification.objects.filter(user=self.request.user).order_by('-timestamp')
        except Exception as e:
            #print(f"Error fetching notifications: {e}")
            return Notification.objects.none()

class NotificationDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    lookup_field = 'id'

    def delete(self, request, id, *args, **kwargs):
        try:
            notification = self.queryset.get(id=id, user_id=request.user.id)
            notification.delete()  
            return Response({"message": "Notification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)