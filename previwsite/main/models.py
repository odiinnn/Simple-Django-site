from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    twsub = models.CharField(max_length=50)
    twretweet = models.CharField(max_length=50)
    telsubchannel = models.CharField(max_length=50)
    telsubgroup = models.CharField(max_length=50)
