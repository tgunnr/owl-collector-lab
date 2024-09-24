from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Create your models here.

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toy-detail', kwargs={'pk': self.id})
  
class Owl(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('owl-detail', kwargs={'owl_id': self.id})

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  owl = models.ForeignKey(Owl, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']