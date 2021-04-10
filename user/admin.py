from django.contrib import admin

from .models import Profile, Student, Teacher, Message


admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Message)
