from django.db import models


class FakeFunctionsData(models.Model):
    uuid = models.CharField(max_length=60, unique=True)
    function_name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_function = models.BooleanField(default=True)

    class Meta:
        db_table = "functions_data"
        verbose_name_plural = "Fake Functions Data"
