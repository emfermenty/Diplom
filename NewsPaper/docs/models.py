from django.db import models


class PDF(models.Model):
    name = models.CharField(max_length=255)  # Название файла
    document = models.FileField(upload_to='pdfs/')  # Файл PDF

    def __str__(self):
        return self.name