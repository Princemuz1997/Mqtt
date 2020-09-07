from django.db import models


class Device(models.Model):
    pi_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pi_id)


