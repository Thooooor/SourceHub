# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
#
#
# class Source(models.Model):
#     source_id = models.CharField(max_length=128)
#     source_name = models.CharField(max_length=128)
#
#     upload_user = models.OneToOneField(User, on_delete=models.CASCADE)
#     upload_time = models.DateTimeField(default=timezone.now())
#     download_counts = models.BigIntegerField()
#     download_users = models.ManyToManyField(User)
#
#     file = models.FileField()
#
#     class Meta:
#         ordering = ("-source_id", )
#
#     def __str__(self):
#         return self.source_name
#
#
# class Course(models.Model):
#     course_id = models.CharField(max_length=128)
#     course_name = models.CharField(max_length=128)
#     sources = models.ManyToManyField(
#         Source,
#         related_name="courses"
#     )
#
#     class Meta:
#         ordering = ("-course_id", )
#
#     def __str__(self):
#         return self.course_name
#
#
# class Semester(models.Model):
#     semester_id = models.CharField(max_length=128)
#     semester_name = models.CharField(null=False, max_length=128)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     courses = models.ManyToManyField(
#         Course,
#         related_name="semesters"
#     )
#
#     class Meta:
#         ordering = ("-semester_id", )
#
#     def __str__(self):
#         return self.semester_name
