from django.shortcuts import render
from website.models import Pessoa
from website.models import Ongs

# Create your views here.

def pagina_index(request):


    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)


    
    return render(request, 'index.html')

def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()
    
    contexto = {
        'pessoas': pessoas
    }
    return render(request, '/pessoas.html', contexto)











def pagina_ong(request):


    if request.method == 'POST':
        ong = Ongs()
        ong.resp_ong = request.POST.get('resp_ong')
        ong.nome_ong = request.POST.get('nome_ong')
        ong.email_ong = request.POST.get('email_ong')
        ong.str_cep_ong = request.POST.get('str_cep_ong')
        ong.str_numero_ong = request.POST.get('str_numero_ong')
        ong.complemento_ong = request.POST.get('complemento_ong')
        ong.telefone_ong = request.POST.get('telefone_ong')        
        ong.trabalho_ong = request.POST.get('trabalho_ong')
        ong.hrs_ong = request.POST.get('hrs_ong')
        ong.save()

        contexto = {
            'nome': ong.nome
        }
        return render(request, 'ong.html', contexto)


    
    return render(request, 'ong.html')

def pagina_ong(request):
    ongs = Ongs.objects.filter(ativo=True).all()
    
    contexto = {
        'ongs': ongs
    }
    return render(request, '/ong.html', contexto)