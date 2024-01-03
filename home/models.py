from django.db import models

class reg(models.Model):
    # empcode = models.IntegerField()
    username = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    # is_active = models.IntegerField(null=True)

    def __str__(self):  
        return self.username
    empAuth_object = models.Manager()
