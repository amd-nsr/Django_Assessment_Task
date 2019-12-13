from django.db import models

class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploaded/')

    def __str__(self):
        return self.title
