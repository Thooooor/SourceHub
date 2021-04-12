from django.db import models
from django.contrib.auth.models import User

from course.models import Course
from school.models import School


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    student_id = models.CharField(max_length=128)
    student_name = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)
    school = models.ForeignKey(School, blank=True, on_delete=models.CASCADE, related_name="students", null=True)

    class Meta:
        ordering = ("-student_id", )

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")
    teacher_id = models.CharField(max_length=128)
    teacher_name = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course, related_name="teachers", blank=True)
    school = models.ForeignKey(School, blank=True, on_delete=models.CASCADE, related_name="teachers", null=True)

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
    title = models.CharField(max_length=128)
    body = models.TextField()
    send = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_messages", null=True, blank=True)
    receive = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recv_messages", null=True, blank=True)
    send_time = models.TimeField(auto_now=True)
    read_time = models.TimeField(null=True, blank=True)
    message_status = models.CharField(default="unread", max_length=128)

    class Meta:
        ordering = ("-send_time",)

    def __str__(self):
        return self.title
