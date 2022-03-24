from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30, db_column="NOME")
    rg = models.CharField(max_length=9, db_column="RG")
    cpf = models.CharField(max_length=11, db_column="CPF")
    data_nascimento = models.DateField(db_column="DATA_NASCIMENTO")

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    codigo_curso = models.CharField(max_length=10, db_column="CODIGO_CURSO")
    descricao = models.CharField(max_length=100, db_column="DESCRICAO")
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null= False, default='B', db_column="NIVEL")

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    Periodo = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=Periodo, blank=False, null= False, default='M', db_column="PERIODO")
