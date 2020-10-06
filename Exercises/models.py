from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.

class Exercise(PolymorphicModel):

    title = models.CharField(max_length=120)
    text = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    referance = models.TextField()
    status = models.CharField(max_length=10, default="Draft", editable=False)
    slug = models.SlugField() #human-friendly URL

    def __str__(self) -> str:
        return self.title


class Matematica(Exercise):

    class Argomento(models.TextChoices):
        matrici = 'MAT', ('Matrici')
        stu_func = 'FUN', ('Studio di funzioni')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, default=Argomento.matrici)
    dim = models.TextField()
    grafico = models.FileField(blank=True)

    def __str__(self) -> str:
        return "Matematica"

    def desc(self):
        return """ La regina delle scienze. Senza di lei non esisterebbe nessuna teoria. """


class Chimica_Organica(Exercise):

    class Argomento(models.TextChoices):
        alcani = 'CAN', ('Alcani')
        alcheni = 'CHE', ('Alcheni')
        alchini = 'CHI', ('Alchini')
        aromatici = 'PHS', ('Aromatici')
        carbonile = 'RCO', ('Carbonile')
        sintesi = 'SIN', ('Sintesi')
    
    argomento = models.CharField(max_length=3, choices=Argomento.choices, default=Argomento.sintesi)
    strutture = models.FileField()
    meccanismo = models.FileField(blank=True)
    commento = models.TextField()

    def __str__(self) -> str:
        return "Chimica Organica"

    def desc(self):
        return """ La chimica che si occupa dello studio della chimica del carbonio e come questo interagisca con gli altri elementi della tavola periodica. """

class Chimica_Generale_Analitica(Exercise):

    class Argomento(models.TextChoices):
        elettrochimica = 'ELE', ('Elettrochimica')
        redox = 'RED', ('Reazioni redox')
        theo_atomica = 'ATM', ('Teoria Atomica e Proprietà Periodiche')
        acidi_basi = 'ACB', ('Teorie del pH e tamponi')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, default=Argomento.acidi_basi)
    sistema = models.TextField()
    commento = models.TextField()
    risultato = models.TextField()

    def __str__(self) -> str:
        return "Chimica Generale e Analitica"

    def desc(self):
        return """ La chimica che si occupa dei vari equilibri in soluzione acquosa """

class Chimica_Fisica(Exercise):

    class Argomento(models.TextChoices):
        elettrodi = 'ELE', ('Elettrodi')
        gas = 'GAS', ('Teorie dei gas')
        termodinamica = 'THM', ('Termodinamica e termochimica')

    argomento = models.CharField(max_length=3, choices=Argomento.choices, default=Argomento.gas)
    sistema = models.TextField()
    commento = models.TextField()
    risultato = models.TextField()

    def __str__(self) -> str:
        return "Chimica Fisica"

    def desc(self):
        return """ La chimica che si occupa di studiare la fisica che sottostà ai diversi eventi chimici """

import sys, inspect

materie = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__ and member.__name__ != 'Exercise')

def get_modello(nome):
    for materia, modello in materie:
        if materia == nome:
            return modello
    raise Exception("Materia inesistente")