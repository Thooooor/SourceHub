from django.db import models
from django.contrib.auth.models import User

from course.models import Course


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    student_id = models.CharField(max_length=128)
    student_name = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    class Meta:
        ordering = ("-student_id", )

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")
    teacher_id = models.CharField(max_length=128)
    teacher_name = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course, related_name="teachers", blank=True)

    class Meta:
        ordering = ("-teacher_id", )

    def __str__(self):
        return self.teacher_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user_type = models.CharField(max_length=128)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class Message(models.Model):
    message_id = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    body = models.TextField()
    send = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_message", null=True, blank=True)
    receive = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recv_message", null=True, blank=True)
    send_time = models.TimeField(auto_now=True)
    read_time = models.TimeField(null=True)
    status = models.CharField(default="Unread", max_length=128)

    class Meta:
        ordering = ("-message_id",)
