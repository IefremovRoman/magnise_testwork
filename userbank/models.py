from django.db import models
from passlib.hash import pbkdf2_sha256


class User(models.Model):

    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    register_date = models.DateTimeField(auto_now_add=True)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
