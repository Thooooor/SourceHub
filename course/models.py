from django.db import models


class Semester(models.Model):
    semester_id = models.CharField(max_length=128)
    semester_name = models.CharField(null=False, max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ("-semester_id", )

    def __str__(self):
        return self.semester_name


class Course(models.Model):
    course_id = models.CharField(max_length=128)
    course_name = models.CharField(max_length=128)
    semesters = models.ManyToManyField(Semester, related_name="courses")

    class Meta:
        ordering = ("-course_id", )

    def __str__(self):
        return self.course_name
