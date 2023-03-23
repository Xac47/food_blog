from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_photo/')
    name = models.TextField(max_length=40)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


