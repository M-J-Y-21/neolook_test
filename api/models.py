from django.db import models

class Recording(models.Model):
    video_file = models.FileField(upload_to='recordings/')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)