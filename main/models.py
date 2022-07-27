from django.db import models
#from json import tool

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
    objects = None

    class Meta:
        verbose_name='фильм'
        verbose_name_plural='фильмы'

    title = models.CharField(max_length=200,unique=True,verbose_name="Название")
    description = models.TextField(max_length=5000,blank=True,verbose_name="Описание фильмы")
    duration=models.DurationField(blank=True,verbose_name="Продолжительность")

    directors = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True,
                                  related_name="movies")

    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount

    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name='отзыв'
        verbose_name_plural='отзывы'
    text = models.TextField(verbose_name="Текст отзыва")
    stars=models.IntegerField(default=1)
    author = models.CharField(max_length=100, null=True, blank=True, default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='reviews')

    def __str__(self):
        return f"{self.author}-{self.movie}"


