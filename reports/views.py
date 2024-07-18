from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Report, Comment
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Report.objects.all().order_by('-timestamp')
        return Report.objects.filter(user=self.request.user).order_by('-timestamp')

    @action(detail=True, methods=['get'])
    def comment_reports(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        reports = Report.objects.filter(comment=comment)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
