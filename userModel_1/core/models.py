from django.db import models

from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    text = models.TextField('Texto')

    def __str__(self):
        return self.title