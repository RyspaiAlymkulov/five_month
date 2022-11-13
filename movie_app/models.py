from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    duration = models.DurationField(verbose_name=None)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)

    def detail_link(self):
        return f'http://127.0.01:8000/api/v1/movies/{self.id}/'