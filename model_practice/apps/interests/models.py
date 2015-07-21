from django.db import models

#Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateField()
	# class Meta:
	# 	db_table = 'interests'

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	age = models.IntegerField()
	created_at = models.DateField()
	occupation = models.CharField(max_length=50)
	interest = models.ForeignKey(Interest)

	# class Meta:
	# 	db_table = 'users'
