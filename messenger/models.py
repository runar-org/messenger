from django.db import models


class Message(models.Model):
    ciphertext = models.BinaryField(max_length=None)
    identifier = models.BinaryField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    default_key = models.BooleanField()
    attempts = models.IntegerField(default=0)

    MAX_ATTEMPTS = 5

    def __bytes__(self):
        return self.ciphertext
