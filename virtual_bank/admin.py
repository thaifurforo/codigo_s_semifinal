# from django.contrib import admin
# from virtual_bank.models import Account, Customer

# # Register your models here.
# class CustomerAdmin(admin.ModelAdmin):
#   # Campos que podem ser inseridos / alterados pelo usuário:
#   fields = ('tipo', 'cpf_cnpj', 'nome_razao_social', 'endereco', 'telefone', 'email', 'data_nascimento')
#   # Campos a serem exibidos ao usuário no Admin:
#   list_display = ('id', 'cpf_cnpj', 'nome_razao_social')
#   # Campos que podem ser utilizados para pesquisa
#   search_fields = ('tipo', 'cpf_cnpj', 'nome_razao_social', 'email', 'data_nascimento')
#   # Número de itens a serem exibidos por página
#   list_per_page = 20

# class AccountAdmin(admin.ModelAdmin):
#   # Campos que podem ser inseridos / alterados pelo usuário
#   fields = ('cliente', 'conta_ativa', 'data_abertura', 'data_encerramento')
#   # Campos a serem exibidos ao usuário no Admin:
#   list_display = ('numero_completo_conta', 'cliente', 'conta_ativa', 'saldo')
#   # Campos que podem ser utilizados para pesquisa
#   search_fields = ('numero_conta_sem_dv', 'numero_completo_conta', 'cliente', 'conta_ativa', 'saldo', 'data_abertura', 'data_encerramento')
#   # Número de itens a serem exibidos por página
#   list_per_page = 20

    
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Account, AccountAdmin)