from django.db import models

class reg(models.Model):
    # empcode = models.IntegerField()
    username = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    # is_active = models.IntegerField(null=True)

    def __str__(self):  
        return self.username
    empAuth_object = models.Manager()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
