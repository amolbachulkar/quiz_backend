from __future__ import unicode_literals
from django.db import models
from quiz.models import Quiz


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Question', max_length=3000)
    options = models.CharField('Options', max_length=3000,)
    correct_option = models.CharField('Correct option. Max 300 characters', max_length=300,)
    quiz = models.ForeignKey(Quiz, db_index=True,on_delete=models.CASCADE)
    points = models.IntegerField( default=0)

    def __str__(self):
        return self.name
