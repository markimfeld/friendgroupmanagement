from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
def __str__(self): return self.name 

class Category(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Meeting(models.Model):
    date = models.DateField()
    topic = models.CharField(max_length=64)
    offering = models.FloatField()
    tithe = models.FloatField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ManyToManyField(Person, through='Attendance')

    def __str__(self):
        return self.topic


class Attendance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="attendances")
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.person.first_name
