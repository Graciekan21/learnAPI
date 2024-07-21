from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from LearnAPI.permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, CommentDetailSerializer
from reports.serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from reports.models import Report


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
