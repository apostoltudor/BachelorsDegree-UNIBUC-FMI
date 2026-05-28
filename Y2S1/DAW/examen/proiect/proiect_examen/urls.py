from django.contrib import admin
from django.urls import path
from examen_aplicatie.views import lista_studenti, cursuri_student, adauga_curs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_studenti, name='lista_studenti'), #ex 5
    path('student/<int:student_id>/', cursuri_student, name='cursuri_student'), #ex 6
    path('adauga-curs/', adauga_curs, name='adauga_curs'), #ex 7
]