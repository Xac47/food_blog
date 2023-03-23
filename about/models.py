from ckeditor.fields import RichTextField
from django.db import models


class About(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    mini_content = RichTextField()
    main_image = models.ImageField('Главное фото', upload_to='about/')
    left_image = models.ImageField('Левое фото', upload_to='about/')
    right_image = models.ImageField('Правое фото', upload_to='about/')

    facebook = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    youtube = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)

    address = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
