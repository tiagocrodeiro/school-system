from django.db import models



# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.CharField(max_length=10)
    end = models.CharField(max_length=50)
    cep = models.CharField(max_length=11)
    email = models.CharField(max_length=40)


class Documentos(models.Model):
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    cnh = models.CharField(max_length=11)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.SET_NULL, null=True)


class Aluno(models.Model):
    mat = models.IntegerField()
    nome = models.CharField(max_length=50)
    data_nascimento = models.CharField(max_length=10)
    ano_letivo = models.CharField(max_length=6)

class Professor(models.Model):
    mat = models.IntegerField()
    nome = models.CharField(max_length=50)
    aluno = models.ManyToManyField(Aluno)

class Disciplina(models.Model):
    id_disc = models.IntegerField()
    tipo = models.CharField(max_length=20)
    aluno = models.ManyToManyField(Aluno)
    professor = models.ManyToManyField(Professor)


class Turna(models.Model):
    id_turma = models.IntegerField()
    aluno = models.ManyToManyField(Aluno)
    professor = models.ManyToManyField(Professor)

class Notas(models.Model):
    nota = models.FloatField()
    diciplina = models.ManyToManyField(Disciplina)
    aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    bimestre = models.CharField(max_length=6)
class Mensalidade():
    valor = models.FloatField()

class Responsavel():
    pai = models.ManyToManyField(Pessoa)
    mae = models.ManyToManyField(Pessoa)
    menalidade = models.ForeignKey("Mensalidade", on_delete=models.CASCADE)
    status = models.CharField(max_length=4)


