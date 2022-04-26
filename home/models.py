from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    tittle = models.CharField(max_length=256)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tittle


class Ranking(models.Model):
    RANK_NUM = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ruser')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='rpost')
    rank = models.IntegerField(choices=RANK_NUM)

    def __str__(self):
        return f'{self.user} rank for {self.post} is {self.rank}'
