from django.contrib import admin
from estoque.models import Materiais, Revenda, Saida

admin.site.register(Materiais)

admin.site.register(Revenda)
admin.site.register(Saida)