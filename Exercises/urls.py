from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *


class ExcerciseListView(ListView):
    def get_queryset(self):
        return get_modello(self.kwargs['materia']).objects.filter(argomento=self.kwargs['argomento'])

class ExerciseDetailView(DetailView):
    def get_queryset(self):
        return get_variabili(self.kwargs['materia'])


urlpatterns = [
    path('', post_views.homepage, name='homepagne'), #homepage

    path('<str:materia>/<str:argomento>', ExcerciseListView.as_view(
        template_name="list.html", paginate_by = 3), name='list'),

    path('<int:id>/<slug:slug>/', ExerciseDetailView.as_view(
        template_name="single.html"), name='single'), # Post singoli
    #È da cambiare il link... Metti che sfiga vuole che tu abbia due id e due indici uguali in due materie diverse... Sei fottuto
    #TODO: change link


    path('contatti/', post_views.contact, name='contacts'), # Sezione contatti
]
