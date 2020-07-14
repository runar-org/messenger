from django.db import models

class Encryption(models.Model):
    key = models.CharField(max_length=500)
    def __str__(self):
        return self.key

class Message(models.Model):
    encryption = models.ForeignKey(Encryption, on_delete=models.CASCADE)
    ciphertext = models.CharField(max_length=500)
    def __str__(self):
        return self.ciphertext