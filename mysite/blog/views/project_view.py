from django.http import HttpResponse
from django.views import generic

class ProjectView(generic.View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1> Agora voçê está na rota de Projetos </h1>")