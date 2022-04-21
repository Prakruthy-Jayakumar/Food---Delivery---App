from django.db import models

class Gallery(models.Model):
    img_name=models.CharField(max_length = 250)
    img = models.ImageField(upload_to='Imagesss')
    description=models.TextField()

    def __str__(self):
        return self.img_name


class Chef(models.Model):
    chef_name=models.CharField(max_length = 250)
    img = models.ImageField(upload_to='Imagesss')
    chef_designation=models.TextField()

    def __str__(self):
        return self.chef_name



class Specials(models.Model):
    special_name=models.CharField(max_length = 250)
    img = models.ImageField(upload_to='Imagesss')
    special_desc=models.TextField()

    def __str__(self):
        return self.special_name

class District(models.Model):
    dist_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dist_name

class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=40)

    def __str__(self):
        return self.place_name

class Food(models.Model):
    name=models.CharField(max_length = 250)
    img = models.ImageField(upload_to='Imagesss')
    desc=models.TextField()
    qty = models.IntegerField()
    price_food = models.FloatField()

    def __str__(self):
        return self.name

class Price(models.Model):
    food = models.ForeignKey(Food,on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField()

class Order(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    district = models.ForeignKey(District,on_delete=models.SET_NULL, blank=True, null=True)
    place = models.ForeignKey(Place,on_delete=models.SET_NULL, blank=True, null=True)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    # price = models.ForeignKey(Price,on_delete=models.SET_NULL, blank=True, null=True)
    qty = models.IntegerField()


    def __str__(self):
        return self.name