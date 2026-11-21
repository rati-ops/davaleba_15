from django.db import models

class Movie(models.Model):
    title = models.CharField()
    genre = models.CharField()
    duration_minutes = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Viewer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()
    is_subscribed = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE, related_name='viewer')
    score = models.IntegerField()

    def __str__(self):
        return f'{self.score}'
