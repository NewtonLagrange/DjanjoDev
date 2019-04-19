from django.db import models

# Create your models here.


class Question(models.Model):
    """ A question """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Choice(models.Model):
    """ choice relate to choice """
    name = models.CharField(max_length=50)
    num = models.IntegerField(default=0)
    ques = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
