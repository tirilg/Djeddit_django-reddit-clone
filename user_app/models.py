from django.db import models
from secrets import token_urlsafe

class PasswordReset(models.Model):
    email = models.CharField(max_length=100)
    token = models.CharField(max_length=40, default=token_urlsafe)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Active: {self.active} // Token: {self.token}"