from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Notification
        fields = ["id", "user", "username", "message", "is_read", "post",
                  "timestamp"]
