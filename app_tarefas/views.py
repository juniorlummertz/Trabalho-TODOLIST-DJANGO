from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Tarefa


def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('novo_titulo', '').strip()
        if titulo:
            Tarefa.objects.create(titulo=titulo)
        return redirect('home')

    tarefas = Tarefa.objects.all().order_by('concluida', '-id')
    return render(request, 'lista.html', {'tarefas': tarefas})


@require_POST
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.concluida = True
    tarefa.save(update_fields=['concluida'])
    return redirect('home')


@require_POST
def deletar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('home')
