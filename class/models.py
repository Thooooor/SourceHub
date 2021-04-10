from django.db import models


class Class(models.Model):
    class_id = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128)

    class Meta:
        ordering = ("-class_id", )

    def __str__(self):
        return self.class_name
