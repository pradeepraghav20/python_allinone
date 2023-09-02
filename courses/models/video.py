from django.db import models
from .courses import Course
class Video(models.Model):
     title  = models.CharField(max_length = 100 , null = False)
     serial_number=models.IntegerField(null=False)
     video_id=models.CharField(max_length=20,null=False)
     is_preview=models.BooleanField(default=False)
     course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

     def __str__(self):
         return self.title

