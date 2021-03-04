from django.db import models


class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Quiz name', max_length=300,)
    description = models.CharField('Quiz description', max_length=3000,)

    def __str__(self):
        return self.name
