from django.db import models

# Create your models here.


from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    author2 = models.CharField(max_length=200,default='sdsd')

    long_text=models.TextField(default='')


    def __str__(self):
        return '%s - %s' % (self.pub_date,self.author)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)