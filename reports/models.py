from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_content = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    reason = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} reported: {self.reason}'
