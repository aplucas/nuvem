from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Arquivo


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proj'] = 'Projeto Python'
        return context


class ListaPageView(TemplateView):
    template_name = 'lista.html'


# REPOSITORIO

class ArquivoListView(ListView):
    model = Arquivo


class ArquivoDetailView(DetailView):
    model = Arquivo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArquivoCreateView(CreateView):
    model = Arquivo
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('arquivo-list')


class ArquivoUpdateView(UpdateView):
    model = Arquivo
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('arquivo-list')


class ArquivoDeleteView(DeleteView):
    model = Arquivo

    def get_success_url(self):
        return reverse_lazy('arquivo-list')
