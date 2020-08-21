from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.first_name


class Meeting(models.Model):
    date = models.DateField()
    topic = models.CharField(max_length=64)
    offering = models.FloatField()
    tithe = models.FloatField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ManyToManyField(Person, through='Attendance')


class Attendance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)