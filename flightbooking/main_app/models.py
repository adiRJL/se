# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
'''class Session(models.Model):
	check_in = models.DateField(default=datetime.now())
	check_out = models.DateField(default=datetime.now())

	def __str__(self):
		return (str(self.pk))'''

class User(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField(default = 0)
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)

	def __str__(self):
		return self.name + " " +self.age

class Flight(models.Model):
	airlines = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)

	departure_city = models.CharField(max_length = 50)
	arrival_city = models.CharField(max_length = 50)

	departure_date = models.DateField(default=datetime.now())

	departure_time = models.TimeField(default = datetime.time(datetime.now()))
	arrival_time = models.TimeField(default = datetime.time(datetime.now()))

	startPrice = models.FloatField(default = 0.0)
	endPrice = models.FloatField(default = 0.0)

	image = models.ImageField(upload_to = 'static/main_app/images', null=True, blank=True)

	def __str__(self):
		return (self.airlines + " " +self.name + " " + self.departure_city + " " 
		+ self.arrival_city)





