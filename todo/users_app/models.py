from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.last_name} | {self.first_name} | {self.birthday_year}'


class Biography(models.Model):
    text = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Brend(models.Model):
    name = models.CharField(max_length=64)
    users = models.ManyToManyField(User)
