from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
