from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=255)
    service_time = models.DateTimeField()
    expiration_time = models.DateTimeField()
    is_serviced = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Notification(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Violation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    issue = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
