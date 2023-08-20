from django.db import models

# Create your models here.

class ElectronicsSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id

class FashionSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id
    

class SportsAndLeisureSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id
    

class WatchesSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id


class AppliancesSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id



class Category(models.Model):
    id = models.CharField(max_length=50, blank=False, primary_key=True)
    electronics_sub_category = models.ManyToManyField(ElectronicsSubCategory, blank=True)
    fashion_sub_category = models.ManyToManyField(FashionSubCategory, blank=True)
    watches_sub_category = models.ManyToManyField(WatchesSubCategory, blank=True)
    sports_and_leisure_sub_category = models.ManyToManyField(SportsAndLeisureSubCategory, blank=True)
    appliances_sub_category = models.ManyToManyField(AppliancesSubCategory, blank=True)

    def __str__(self):
        return self.id
    