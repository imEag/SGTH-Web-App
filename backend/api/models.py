from django.db import models


class Professional(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.PositiveIntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    responsible = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        db_column='responsible'
    )
    image = models.ImageField(upload_to='device_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.serial}"
