from django.db import models


class Role(models.IntegerChoices):
    ADMIN = 0, 'ADMIN'
    DEV = 1, 'DEV'


class UserMixin(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    role = models.IntegerField(default=Role.DEV, choices=Role.choices)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, db_index=True)
    is_staff = models.BooleanField(default=True)

