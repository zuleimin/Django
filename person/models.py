from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

# Create your models here.

class Person(models.Model):
    person_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Category(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE,default=0)
    category_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
