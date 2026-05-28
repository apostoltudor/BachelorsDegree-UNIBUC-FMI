from django.db import models

#ex 1
class Student(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    email = models.EmailField()
    anul_inscrierii = models.IntegerField()

    def __str__(self):
        return f"{self.nume} {self.prenume}"

class Curs(models.Model):
    denumire = models.CharField(max_length=100)
    numar_credite = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='cursuri')

    def __str__(self):
        return self.denumire
    
    
#ex 2

#python manage.py createsuperuser
#admin_examen
#parola5539