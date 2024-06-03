from django.shortcuts import render, redirect
from aplicativo.forms import AlunosForm
from aplicativo.models import Alunos
from django.http import HttpResponse
#https://docs.djangoproject.com/en/5.0/topics/
from django.contrib import messages


def home(request):
    data = {}
    data['db'] = Alunos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'forms.html', data)

def create(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def deletar(request,id):
    db = Alunos.objects.get(id=id)
    db.delete()
    messages.add_message(request, messages.INFO, 'Atualizado com sucesso!')
    return redirect(home)

def atualizar(request,id):
    if request.method == 'POST':
        form = AlunosForm(request.POST or None)
        if form.is_valid():
            db = Alunos.objects.all().get(id=id)
            db.nome_aluno = form.cleaned_data['nome_aluno']
            db.idade_aluno = form.cleaned_data['idade_aluno']
            db.curso_aluno = form.cleaned_data['curso_aluno']
            db.save()
            messages.add_message(request, messages.INFO, 'Atualizado com sucesso!')
            return redirect(home)
    else:
        data = {}
        data['dados'] = Alunos.objects.get(id=id)
        return render(request, 'atualizar.html', data)
