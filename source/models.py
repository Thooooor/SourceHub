from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from course.models import Course


class Source(models.Model):
    source_id = models.CharField(max_length=128)
    source_name = models.CharField(max_length=128)

    courses = models.ManyToManyField(Course, related_name="sources")

    upload_user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(default=timezone.now)
    download_counts = models.BigIntegerField()

    file = models.FileField()

    class Meta:
        ordering = ("-source_id", )

    def __str__(self):
        return self.source_name
