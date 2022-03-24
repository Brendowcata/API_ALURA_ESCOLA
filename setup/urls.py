from django.contrib import admin
from django.db import router
from django.urls import path, include
from escola.views import AlunoViewSet, CursoViewSet, ListaAlunosMatriculados, MatriculaViewSet, ListaAlunoMatricula
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaAlunoMatricula.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
