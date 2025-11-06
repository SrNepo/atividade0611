from django.contrib import admin
from vendaEnergiaSolar.models import PessoaFisica, PessoaJuridica

# Register your models here.
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_completo',
        'cpf',
        'data_nasc',
        'rg',
        'email',
        'telefone_principal',
        'telefone_secundario',
    )

admin.site.register(PessoaFisica, PessoaFisicaAdmin)

class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_fantasia',
        'cnpj',
        'razao_social',
        'abertura',
        'inscricao_estadual',
        'endereco',
        'cep',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'pais',
    )

admin.site.register(PessoaJuridica, PessoaJuridicaAdmin)
