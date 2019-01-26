from django.db import models

class Kitchen(models.Model):
	length=models.FloatField()
	width=models.FloatField()
	cost =models.FloatField()
	total_price =models.FloatField()

class Bedroom(models.Model):
	length=models.FloatField()
	width=models.FloatField()
	cost=models.FloatField()
	total_price =models.FloatField()


class Hall(models.Model):
	length=models.FloatField()
	width=models.FloatField()
	cost =models.FloatField()
	total_price =models.FloatField()

	
class Handles(models.Model):
	name = models.CharField(max_length=512, null=True, blank=True)
	description =models.TextField(null=True, blank=True)
	photos = models.TextField()
	price =models.FloatField(null=True, blank=True)
	totalprice =models.FloatField(null=True, blank=True)
	quantity = models.IntegerField()
	kitchen_handles = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

class Doors(models.Model):
	name = models.CharField(max_length=512, null=True, blank=True)
	description =models.TextField(null=True, blank=True)
	photos = models.TextField()
	price =models.FloatField(null=True, blank=True)
	totalprice =models.FloatField(null=True, blank=True)
	quantity = models.IntegerField()
	kitchen_doors = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

class Bedroom_handles(models.Model):
	name = models.CharField(max_length=512, null=True, blank=True)
	description =models.TextField(null=True, blank=True)
	photos = models.TextField()
	price =models.FloatField(null=True, blank=True)
	totalprice =models.FloatField(null=True, blank=True)
	quantity = models.IntegerField()
	bedroom_handles = models.ForeignKey(Bedroom, on_delete=models.CASCADE)

class Bedroom_doors(models.Model):
	name = models.CharField(max_length=512, null=True, blank=True)
	description =models.TextField(null=True, blank=True)
	photos = models.TextField()
	price =models.FloatField(null=True, blank=True)
	totalprice =models.FloatField(null=True, blank=True)
	quantity = models.IntegerField()
	bedroom_doors = models.ForeignKey(Bedroom, on_delete=models.CASCADE)

class Hall_handles(models.Model):
	name = models.CharField(max_length=512, null=True, blank=True)
	description =models.TextField(null=True, blank=True)
	photos = models.TextField()
	price =models.FloatField(null=True, blank=True)
	totalprice =models.FloatField(null=True, blank=True)
	quantity = models.IntegerField()
	hall_handles = models.ForeignKey(Hall, on_delete=models.CASCADE)

class Hall_doors(models.Model):
	name = models.CharField(max_length=512, null=True, blank=True)
	description =models.TextField(null=True, blank=True)
	photos = models.TextField()
	price =models.FloatField(null=True, blank=True)
	totalprice =models.FloatField(null=True, blank=True)
	quantity = models.IntegerField()
	hall_doors = models.ForeignKey(Hall, on_delete=models.CASCADE)

class Checkout(models.Model):
	fullname=models.CharField(max_length=200)
	email=models.CharField(max_length=700)
	address=models.CharField(max_length=1000)
	state=models.CharField(max_length=280)
	city=models.CharField(max_length=200)
	zipp=models.IntegerField()
	nameoncard=models.CharField(max_length=250)
	cardnumber=models.IntegerField()
	expyear=models.IntegerField()
	expmonth=models.CharField(max_length=10)
	cvv=models.IntegerField()	

