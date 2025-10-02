from pyexpat import model
from django.db import models

# Create your models here.



class Xodim(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Mijoz(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Tovar(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    soni = models.PositiveIntegerField()


    def __str__(self):
        return self.name

class Zakaz(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return self.name

class Statistics(models.Model):
    xodim = models.ForeignKey(Xodim,on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    zakaz = models.ForeignKey(Zakaz,on_delete=models.CASCADE)


    # def __str__(self):
    #     return self.zakaz