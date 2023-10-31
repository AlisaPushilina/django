from django.db import models
from django.db import models


class Subjects(models.Model):
    id_subject = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Предмет: {self.name}, Id: {self.id_subject}'


class Olympiads(models.Model):
    id_olympiad = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id_subject = models.ForeignKey('Subjects', on_delete=models.CASCADE)
    dates_of_event = models.CharField(max_length=100)
    dates_of_registration = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return f'Олимпиада: {self.name}, Сроки регистрации: {self.dates_of_registration}, ' \
               f'Сроки проведения: {self.dates_of_event}, Уровень: {self.level}'


class Results(models.Model):
    id_result = models.AutoField(primary_key=True)
    result = models.CharField(max_length=100)
    id_student = models.ForeignKey('Students', on_delete=models.CASCADE)
    id_olympiad = models.ForeignKey('Olympiads', on_delete=models.CASCADE)


class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    selected_subject = models.JSONField()
    selected_olympiad = models.JSONField()

    number_class = models.IntegerField()
    letter_of_class = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name} {self.id_class}'


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name}'
# Create your models here.
