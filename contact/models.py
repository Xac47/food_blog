from django.db import models


class SubscribeEmail(models.Model):
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email


class GetInTouch(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Get In Touch'
        verbose_name_plural = 'Get In Touch'

    def __str__(self):
        return f'{self.name} {self.email}'
