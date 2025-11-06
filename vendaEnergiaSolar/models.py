from django.db import models

# Create your models here.
class PessoaFisica(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    rg = models.CharField(max_length=20)
    email = models.EmailField()
    telefone_principal = models.CharField(11)
    telefone_secundario = models.CharField(11)

class PessoaJuridica(models.Model):
    nome_fantasia = models.CharField(255)
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=150)
    abertura = models.DateField()
    inscricao_estadual = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)

