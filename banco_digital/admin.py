from django.contrib import admin

from banco_digital.models import Cliente, Conta

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
  fields = ('tipo', 'cpf_cnpj', 'nome_razao_social', 'endereco', 'telefone', 'email')
  list_display = ('id', 'cpf_cnpj', 'nome_razao_social')

class ContaAdmin(admin.ModelAdmin):
  list_display = ('numero_completo_conta', 'cliente', 'conta_ativa', 'saldo')
  fields = ('cliente', 'conta_ativa', 'saldo')
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Conta, ContaAdmin)