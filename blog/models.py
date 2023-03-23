from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField('Категория', max_length=150, unique=True)
    slug = models.SlugField(max_length=250)
    parent = TreeForeignKey(
        'Category',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-posts', kwargs={'slug': self.slug})

    def get_posts(self):
        return self.post_set.all()


class Tag(models.Model):
    name = models.CharField('Тег', max_length=100, unique=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField('Заголовок', max_length=200)
    image = models.ImageField('Фото', upload_to='images/%Y/%m/%d/')
    text = models.TextField('Описание')
    create_at = models.DateTimeField('Опубликован', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='post', verbose_name='Теги')
    auther = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField('Имя', max_length=60)
    email = models.CharField(max_length=120)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    create_at = models.DateTimeField('Обуликовано', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name}, {self.message}'
