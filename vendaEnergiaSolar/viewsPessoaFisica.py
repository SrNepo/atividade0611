from django.shortcuts import redirect, render
from vendaEnergiaSolar.models import PessoaFisica

# Create your views here.
def index(request):
    pessoasfisicas = PessoaFisica.objects.all()
    return render(request, "vendaEnergiaSolar/index.html",{"pessoasfisicas":pessoasfisicas})

def cadastrarPessoaFisica(request):
    return render(request, "vendaEnergiaSolar/cadastrarPessoaFisica.html")

def adicionarPessoaFisica(request):
    nome_completo = request.POST.get('nome_completo')
    cpf = request.POST.get('cpf')
    data_nasc = request.POST.get('data_nasc')
    rg = request.POST.get('rg')
    email = request.POST.get('email')
    telefone_principal = request.POST.get('telefone_principal')
    telefone_secundario = request.POST.get('telefone_secundario')

    pessoa = PessoaFisica(
        nome_completo=nome_completo,
        cpf=cpf,
        data_nasc=data_nasc,
        rg=rg,
        email=email,
        telefone_principal=telefone_principal,
        telefone_secundario=telefone_secundario
    )
    pessoa.save()
    return redirect('index')

def deletarPessoaFisica(request, id):
    pessoa = PessoaFisica.objects.get(id = id)
    pessoa.delete()
    pessoasfisicas = PessoaFisica.objects.all()
    return render(request, "vendaEnergiaSolar/index.html",{"pessoasfisicas":pessoasfisicas})

def atualizarPessoaFisica(request, id):
    pessoa = PessoaFisica.objects.get(id=id)
    return render(request, "vendaEnergiaSolar/atualizarPessoaFisica.html",{"pessoa":pessoa})

def aplicarAtualizacaoPessoaFisica(request, id):
    nome_completo = request.POST.get('nome_completo')
    cpf = request.POST.get('cpf')
    data_nasc = request.POST.get('data_nasc')
    rg = request.POST.get('rg')
    email = request.POST.get('email')
    telefone_principal = request.POST.get('telefone_principal')
    telefone_secundario = request.POST.get('telefone_secundario')

    pessoa = PessoaFisica.objects.get(id=id)
    pessoa.nome_completo = nome_completo
    pessoa.cpf = cpf
    pessoa.data_nasc = data_nasc
    pessoa.rg = rg
    pessoa.email = email
    pessoa.telefone_principal = telefone_principal
    pessoa.telefone_secundario = telefone_secundario
    pessoa.save()
    return redirect('index')
