from django.db import models

class Message(models.Model):
    ciphertext = models.BinaryField(max_length=None)
    identifier = models.BinaryField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    def __bytes__(self):
        return self.ciphertext
