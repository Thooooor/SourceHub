from django.db import models

from school.models import School


class Semester(models.Model):
    semester_id = models.BigAutoField(primary_key=True)
    semester_name = models.CharField(null=False, max_length=128)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ("-semester_id", )

    def __str__(self):
        return self.semester_name


class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=128)
    semesters = models.ManyToManyField(Semester, related_name="courses", blank=True)
    course_status = models.CharField(max_length=128, default="close")
    school = models.ForeignKey(School, blank=True, null=True, related_name="courses", on_delete=models.CASCADE)

    class Meta:
        ordering = ("course_id", )

    def __str__(self):
        return self.course_name
