from django.contrib import admin
from .models import *

# Register your models here.

class Admin(admin.ModelAdmin):
    
    list_display = ['__str__', 'date', 'argomento']
    list_filter = ['date', 'argomento']
    search_fields = ['title', 'text', 'argomento']

    prepopulated_fields = {"slug": ("title",)}

    class Meta():
        model = Exercise

admin.site.register(Matematica, Admin)
admin.site.register(Chimica_Generale_Analitica, Admin)
admin.site.register(Chimica_Organica, Admin)
admin.site.register(Chimica_Fisica, Admin)
