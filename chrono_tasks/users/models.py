from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator, MinLengthValidator

class User(models.Model):
    name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator(), MaxLengthValidator(255)])
    icon_color = models.CharField(max_length=7, validators=[MinLengthValidator(7), MaxLengthValidator(7)])
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'users'