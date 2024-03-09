from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    # информация о загруженном файле
    file = models.FileField(upload_to='uploads/')
    # дата и время загрузки
    uploaded_at = models.DateTimeField(auto_now_add=True)
