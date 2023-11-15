from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    def score_count(self):
        return self.scores.count()

    def average_score(self):
        return self.scores.aggregate(Avg('score'))['score__avg']


class Score(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scores')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.article} - Score : {self.score} - user: {self.user}"
