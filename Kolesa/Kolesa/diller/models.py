from django.db import models

# Create your models here.
from auth_.models import User
from main.models import Car, City

class AbstractModelDiller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    publications = models.ForeignKey(to="Publications", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
    # def __str__(self):
    #     return self.publications.title

class FavoritesManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Favourites(AbstractModelDiller):

    objects = FavoritesManager

class Publications(models.Manager):
    def order_by_year(self):
        return self.filter().order_by('year')

class Publications(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class ArchiveManager(models.Manager):
    def for_car(self, car):
        return self.filter(car=car)

class Archive(AbstractModelDiller):

    objects = ArchiveManager