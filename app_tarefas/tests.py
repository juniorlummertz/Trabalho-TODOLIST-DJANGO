from django.test import TestCase
from django.urls import reverse

from .models import Tarefa


class TarefaViewsTests(TestCase):
    def test_adiciona_tarefa(self):
        response = self.client.post(reverse('home'), {'novo_titulo': 'Estudar Django'})

        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Tarefa.objects.filter(titulo='Estudar Django').exists())

    def test_conclui_tarefa(self):
        tarefa = Tarefa.objects.create(titulo='Publicar projeto')

        response = self.client.post(reverse('concluir', args=[tarefa.id]))

        tarefa.refresh_from_db()
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(tarefa.concluida)

    def test_remove_tarefa(self):
        tarefa = Tarefa.objects.create(titulo='Tarefa temporária')

        response = self.client.post(reverse('deletar', args=[tarefa.id]))

        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Tarefa.objects.filter(id=tarefa.id).exists())
