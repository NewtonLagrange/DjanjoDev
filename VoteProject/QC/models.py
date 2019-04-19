from django.db import models


# Create your models here.
class MyManage(models.Manager):
    def create_acc(self, name):
        account = self.create(name = name)
        return account


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


class Account(models.Model):
    name = models.CharField(max_length=20)
    manage = MyManage()

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    name = models.CharField(max_length=20)
    account = models.OneToOneField(to=Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=20)
    host = models.ManyToManyField(to=Host)

    def __str__(self):
        return self.name









