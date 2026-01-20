from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    create_add = models.DateTimeField(auto_now_add=True, null=True)
    update_add = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"