from django.db import models

# Create your models here.
class Detail(models.Model):
    username = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class EasyQuestion(models.Model):
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250)
    op1 = models.CharField(max_length=250)
    op2 = models.CharField(max_length=250)
    op3 = models.CharField(max_length=250)
    op4 = models.CharField(max_length=250)
    answer = models.IntegerField(null=False)

class HardQuestion(models.Model):
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250)
    op1 = models.CharField(max_length=250)
    op2 = models.CharField(max_length=250)
    op3 = models.CharField(max_length=250)
    op4 = models.CharField(max_length=250)
    answer = models.IntegerField(null=False)