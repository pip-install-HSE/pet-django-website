from django.db import models


# Create your models here.

class FilterQuestion(models.Model):
    title = models.TextField()
    cur_answer = models.TextField(default=None)

    def __str__(self):
        return f'{self.title}'


class FilterQuestionUnit(models.Model):
    question = models.ForeignKey(to=FilterQuestion, related_name='options', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class PersonalQuestion(models.Model):
    title = models.TextField()
    cur_answer = models.TextField(default=None)

    def __str__(self):
        return f'{self.title}'


class PersonalQuestionUnit(models.Model):
    question = models.ForeignKey(to=PersonalQuestion, related_name='options', on_delete=models.CASCADE)
    text = models.TextField()

    point = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.text}'


class Animal(models.Model):
    name = models.TextField()
    photo = models.ImageField(upload_to='media/')

    point = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'
