from django.db import models


# Create your models here.
class Question(models.Model):
    queestion_text = models.CharField(max_length=256)
    publication_date = models.DateTimeField(verbose_name='date published')


class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
