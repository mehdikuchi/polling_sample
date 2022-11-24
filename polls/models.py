from django.db import models

# Create your models here.
class Question(models.Model):
    QuestionText = models.CharField(max_length=100)
    pub_data = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    