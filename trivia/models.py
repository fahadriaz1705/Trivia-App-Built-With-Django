from django.db import models

# Create your models here.
class Card(models.Model):
    cardId = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300,default='')
    answer = models.CharField(max_length=300,default='')
    hint = models.CharField(max_length=300,default='')

    def __str__(self):
        return self.question