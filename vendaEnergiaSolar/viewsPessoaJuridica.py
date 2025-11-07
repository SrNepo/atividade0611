from django.shortcuts import redirect, render
from vendaEnergiaSolar.models import PessoaFisica, PessoaJuridica

def cadastrarPessoaJuridica(request):
    return render(request, "vendaEnergiaSolar/cadastrarPessoaJuridica.html")

def vizualizarPessoaJuridica(request):
    pessoasjuridicas = PessoaJuridica.objects.all()
    return render(request, "vendaEnergiaSolar/pessoaJuridica.html", {"pessoasjuridicas": pessoasjuridicas})

def adicionarPessoaJuridica(request):
    nome_fantasia = request.POST.get('nome_fantasia')
    cnpj = request.POST.get('cnpj')
    razao_social = request.POST.get('razao_social')
    abertura = request.POST.get('abertura')
    inscricao_estadual = request.POST.get('inscricao_estadual')
    endereco = request.POST.get('endereco')
    cep = request.POST.get('cep')
    logradouro = request.POST.get('logradouro')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    estado = request.POST.get('estado')
    pais = request.POST.get('pais')

    pessoa = PessoaJuridica(
        nome_fantasia=nome_fantasia,
        cnpj=cnpj,
        razao_social=razao_social,
        abertura=abertura,
        inscricao_estadual=inscricao_estadual,
        endereco=endereco,
        cep=cep,
        logradouro=logradouro,
        numero=numero,
        bairro=bairro,
        cidade=cidade,
        estado=estado,
        pais=pais
    )
    pessoa.save()
    return redirect('visualizarPessoaJuridica')

def deletarPessoaJuridica(request, id):
    pessoa = PessoaJuridica.objects.get(id=id)
    pessoa.delete()
    return redirect('visualizarPessoaJuridica')

def atualizarPessoaJuridica(request, id):
    pessoa = PessoaJuridica.objects.get(id=id)
    return render(request, "vendaEnergiaSolar/atualizarPessoaJuridica.html", {"pessoa": pessoa})

def aplicarAtualizacaoPessoaJuridica(request, id):
    nome_fantasia = request.POST.get('nome_fantasia')
    cnpj = request.POST.get('cnpj')
    razao_social = request.POST.get('razao_social')
    abertura = request.POST.get('abertura')
    inscricao_estadual = request.POST.get('inscricao_estadual')
    endereco = request.POST.get('endereco')
    cep = request.POST.get('cep')
    logradouro = request.POST.get('logradouro')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    estado = request.POST.get('estado')
    pais = request.POST.get('pais')

    pessoa = PessoaJuridica.objects.get(id=id)
    pessoa.nome_fantasia = nome_fantasia
    pessoa.cnpj = cnpj
    pessoa.razao_social = razao_social
    pessoa.abertura = abertura
    pessoa.inscricao_estadual = inscricao_estadual
    pessoa.endereco = endereco
    pessoa.cep = cep
    pessoa.logradouro = logradouro
    pessoa.numero = numero
    pessoa.bairro = bairro
    pessoa.cidade = cidade
    pessoa.estado = estado
    pessoa.pais = pais
    pessoa.save()

    return redirect('visualizarPessoaJuridica')

