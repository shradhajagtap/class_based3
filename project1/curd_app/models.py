from django.db import models


class Student(models.Model):
    DIV_CHOICE = [("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")]
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    student_age = models.IntegerField()
    student_address = models.TextField(max_length=50)
    student_div_mode = models.CharField(max_length=2, choices=DIV_CHOICE)


