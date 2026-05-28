from django.shortcuts import render, redirect
from .models import Student
from .forms import CursForm

#ex 5
def lista_studenti(request):
    studenti = Student.objects.all()
    return render(request, 'lista_studenti.html', {'studenti': studenti})

#ex 6
def cursuri_student(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'cursuri_student.html', {'student': student})





#ex 7
def adauga_curs(request):
    if request.method == 'POST':
        form = CursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_studenti')
    else:
        form = CursForm()
    return render(request, 'adauga_curs.html', {'form': form})