from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=256)
    concluida = models.BooleanField(default=False)

    def _str_(self):
        return self.titulo