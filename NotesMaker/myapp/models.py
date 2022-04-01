from django.db import models

class Note(models.Model):
	text = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)
