from django.db import models


class post(models.Model):
    title =  models.CharField(max_length=250,blank=False,null=True)
    description = models.CharField(max_length=250,blank=False,null=True)

    def __str__(self):
        return self.title