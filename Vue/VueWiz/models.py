from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class ResumeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(db_column='title', max_length=180, blank=True, null=True, help_text="Title of the image")
    file = models.FileField(db_column='file', upload_to='media', null=True, blank=True, help_text="Load a resume.")

class VideoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(db_column='title', max_length=180, blank=True, null=True, help_text="Title of the video")
    file = models.FileField(db_column='file', upload_to='media', null=True, blank=True, help_text="Load a video.")

# user 1 - many resume
# user 1 - many videos
