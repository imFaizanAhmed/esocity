from django.db import models

# Create your models here.

class temp_Client():
	id: int
	First_name: str
	Last_name: str
	Company: str
	Tag: str    
    
class Client(models.Model):
	First_name = models.CharField(max_length = 100)
	Last_name = models.CharField(max_length = 100)
	company = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.First_name + " " + self.Last_name + " " + self.company

class Client_tag(models.Model):
 	client = models.ForeignKey(Client, on_delete = models.CASCADE)
 	tag = models.CharField(max_length = 100)
 	
class Tweets(models.Model):
 	client_tag = models.ForeignKey(Client_tag, on_delete = models.CASCADE)
 	text = models.CharField(max_length = 100)
 	polarity = models.CharField(max_length = 100)
 	subjectivity = models.CharField(max_length = 100)
