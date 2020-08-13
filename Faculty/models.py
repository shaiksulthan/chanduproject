from django.db import models

# Create your models here.
class Faculty(models.Model):
	branches = (
		     ("ECE",'ece'),
		     ("CSE",'cse'),
		     ("IT",'it'),
		     ("EEE",'eee')
		)
	Name = models.CharField(max_length=20)
	Age = models.IntegerField()
	Branch = models.CharField(max_length=10,choices = branches)
	Mobile = models.CharField(max_length=10)
	Email = models.EmailField(blank=True)

	def __str__(self):
		return self.Name
