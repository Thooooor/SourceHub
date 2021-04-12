from django.db import models


class School(models.Model):
    school_id = models.BigAutoField(primary_key=True)
    school_name = models.CharField(max_length=128)

    class Meta:
        ordering = ("school_id",)

    def __str__(self):
        return self.school_name
