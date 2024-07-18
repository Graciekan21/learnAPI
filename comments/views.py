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

class CommentReportList(APIView):
    """
    API View to list and create reports related to a specific comment.
    """
    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get(self, request, pk):
        comment = self.get_comment(pk)
        reports = Report.objects.filter(comment=comment)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        comment = self.get_comment(pk)
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment=comment, user=request.user)  # Assuming user is authenticated
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)