from django.db import models


# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)


class Subscriber1(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.surname, self.first_name)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
