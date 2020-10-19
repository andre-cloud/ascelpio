from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *


class ExcerciseListView(ListView):
    def get_queryset(self):
        return get_modello(self.kwargs['materia']).objects.filter(argomento=self.kwargs['argomento'], status='Pubblished').order_by('-date')


urlpatterns = [
    path('', post_views.homepage, name='homepagne'), #homepage

    path('<str:materia>/<str:argomento>', ExcerciseListView.as_view(
        template_name="list.html", paginate_by = 33), name='list'),

    path('<int:id>/<slug:slug>/', DetailView.as_view(
        queryset=Exercise.objects, template_name="single.html"), name='single'), # Post singoli

    path('contatti/', post_views.contact, name='contacts'), # Sezione contatti
]
