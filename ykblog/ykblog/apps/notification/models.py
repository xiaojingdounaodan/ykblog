from django.db import models

from django.conf import settings
import json

from time import time

class Notification(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name="notifications",on_delete=models.CASCADE)

    timestamp = models.FloatField(default=time)
    payload_json = models.CharField(max_length=255)

    def __str__(self):
        return '<Notification {}>'.format(self.pk)

    def get_data(self):
        return json.loads(str(self.payload_json))