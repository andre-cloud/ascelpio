from django.contrib import admin
from .models import *

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='Pubblished')
make_published.short_description = "Pubblica gli esercizi selezionati"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='Draft')
make_draft.short_description = "Non visualizzare gli esercizi selezionati"

class Admin(admin.ModelAdmin):
    
    list_display = ['title', 'date', 'argomento', 'status']
    list_filter = ['date', 'argomento']
    search_fields = ['title', 'text', 'argomento']

    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft]

    class Meta():
        model = Exercise


admin.site.register(Matematica, Admin)
admin.site.register(Chimica_Generale_Analitica, Admin)
admin.site.register(Chimica_Organica, Admin)
admin.site.register(Chimica_Fisica, Admin)
