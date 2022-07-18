from django.db import models

# Create your models here.

class Director(models.Model):
    objects = None

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    name=models.CharField(max_length=70)


    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name='фильм'
        verbose_name_plural='фильмы'

    title = models.CharField(max_length=200,unique=True,verbose_name="Название")
    description = models.TextField(max_length=5000,blank=True,verbose_name="Описание фильмы")
    duration=models.DurationField(blank=True,verbose_name="Продолжительность")

    directors = models.ForeignKey(Director, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name="Режиссеры")

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name='отзыв'
        verbose_name_plural='отзывы'
    text = models.TextField(verbose_name="Текст отзыва")
    author = models.CharField(max_length=100, null=True, blank=True, default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,verbose_name="фильм")

    def __str__(self):
        return f"{self.author}-{self.movie}"


