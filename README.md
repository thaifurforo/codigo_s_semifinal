# Desafio SEMIFINAL /código[s]

O /código[s] é um programa de formação em Python oferecido pela Stone, em parceria com a How Bootcamps, com o objetivo de capacitar pessoas que desejam iniciar o aprendizado na área de tecnologia.

Participando deste programa, ao longo dos últimos meses tive a oportunidade de estudar assuntos como:
- Orientação a objetos
- Tratamento de exceção
- Persistência
- Testes de unidade
- Arquitetura
- Banco de dados
- Django

Para a semifinal do programa, a Stone desafiou os participantes a desenvolverem um API REST similar a um banco digital, onde os clientes possuam contas e façam transferência de valores entre
eles. A API deverá permitir:
- A criação de uma nova conta
- Consulta de todas as contas criadas
- Consulta de saldo de um conta
- Transferência de saldo entre contas
- Consulta das transferências de uma conta (Recebidos e enviados)
  - Com a possibilidade de consultar em um dado período estipulado

Os critérios de avaliação serão:
- Implementação dos requisitos de negócio
- Design da API
- Documentação
  - Readme e comentários pertinentes
- Boas práticas e qualidade
  - Compreensão do código
  - Estrutura do sistema
  - Separação de responsabilidades
  - Dry, Solid, Kiss, Yagni
- Versionamento do código
- Testes de unidade
- Tratamento dos valores decimais
- Tratamento de erros

**Neste repositório se encontra a API que eu desenvolvi para atender ao desafio!**

# Documentação da API

[Acesse aqui as especificações OpenAPI Swagger](docs/swagger.json).

## Funcionalidades
- Criação, atualização, consulta e exclusão de clientes
- Criação, atualização e consulta de contas bancárias
- Criação, consulta e exclusão de transações bancárias
- Consulta de contas bancárias por cliente
- Consulta de transações bancárias por conta
- Filtros, ordenação e pesquisa de dados

## Contato
Em caso de problemas, favor abrir uma [issue](https://github.com/thaifurforo/codigo_s_semifinal/issues).

## Requisitos
A versão do Python utilizada para o desenvolvimento desta API foi a 3.10.4.

As bibliotecas utilizadas para o desenvolvimento desta API constam em [requirements.txt](requirements.txt).

Para realizar a instalação das mesmas, em seu ambiente virtual, digite o comando: `pip install -r requirements.txt`

## Autenticação
A autenticação utilizada para acesso à API é uma do tipo Autenticação Básica HTTP, através de usuário e senha.

## Lista de Models
- [Model com as propriedades do cliente](#cliente)
- [Model com as propriedades do endereços](#endereço)
- [Model com as propriedades da conta bancária](#conta)
- [Model com as propriedades do saldo atual da conta bancária](#saldo)
- [Model com as propriedades da transação bancária](#transação)

## Lista de Validações
- [Validações das propriedades do cliente](#validações-cliente) 
- [Validações das propriedades da conta bancária](#validações-conta) 
- [Validações das propriedades da transação](#validações-transação) 

## Lista de Filtros, Ordenação e Pesquisa de Dados
- [Filtros, ordenação e pesquisa de dados da visualização de clientes](#filtros-clientes) 
- [Filtros, ordenação e pesquisa de dados da visualização de contas bancárias](#filtros-conta) 
- [Filtros, ordenação e pesquisa de dados da visualização de transações](#filtros-transação) 

## Models

### Cliente

O model `Customer` disponibiliza, em suas propriedades, informações de um cliente.

Ao ser serializado, é possível inserir novos clientes, realizar atualizações nos dados dos clientes já existentes,
consultar os clientes e excluí-los, considerando as normas da LGPD.

Pode ser acessado pela rota: `/v1/customer/`.

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada cliente. Chave primária do model.
- customer_type **(string)**: Obrigatório. Tipo de cliente: "PF" se pessoa física ou "PJ" se pessoa jurídica.
- document_number **(string)**: Obrigatório e único. Número do CPF (se pessoa física) ou CNPJ (se pessoa jurídica). Deve ser uma string para que armazene adequadamente os possíveis zeros à esquerda. 
- name **(string)**: Obrigatório. Nome completo (se pessoa física) u Razão social (se pessoa jurídica) do cliente.
- phone_number **(string)**: Obrigatório. Número de telefone do cliente.
- email **(string)**: Obrigatório. Endereço de e-mail do cliente.
- birthdate **(datetime.date)**: Obrigatório caso pessoa física. Data de nascimento do cliente.
- zip_code **(string)**: Obrigatório. CEP do endereço do cliente. Utilizado para consultar o restante do endereço, conforme modelo [Endereço](#endereço).
- door_number **(string)**: Obrigatório. Número da casa/prédio/etc. do endereço do cliente.
- complement **(string)**: Opcional. Complemento do endereço do cliente.

### Endereço

O model `Address` disponibiliza, em suas propriedades, informações de um endereço.

O banco de dados deste modelo registra os endereços completos referentes aos CEPs já inseridos junto ao model [Cliente](#cliente).
Toda vez que um novo CEP é inserido, é realizado uma consulta. Caso o mesmo já exista no banco de dados, nada acontece.
Caso contrário, é realizada automaticamente uma consulta pelo API VIACEP dos demais campos do endereço ao qual o CEP se refere,
e os mesmos são registrados no banco de dados do modelo.

Não há visualização para este model, pois os dados serializados são visualizados juntamente aos do model [Cliente](#cliente) nas requisições GET.

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada endereço. Chave primária do model.
- zip_code **(string)**: Único. CEP do endereço.
- city **(string)**: Cidade a que se refere o CEP.
- district **(string)**: UF (Unidade Federativa) a que se refere o CEP.
- neighborhood **(string)**: Bairro a que se refere o CEP.
- street **(string)**: Logradouro a que se refere o CEP.

### Conta

O model `Account` disponibiliza, em suas propriedades, informações de uma conta bancária.

Ao ser serializado, é possível criar novas contas bancárias, realizar atualizações em alguns dados das contas já existentes e consultar as contas bancárias.
Não é possível excluí-las, pois isto acarretaria em um problema nos registros das transações, que devem ser arquivados por motivos de segurança e regulamentação.
Porém, elas podem ser "encerradas", através da atualização do valor do campo `active_account` para `False`.

Pode ser acessado pela rota: `/v1/account/`.
Também podem ser verificadas todas as contas de um mesmo cliente, pela rota: `/v1/customer/<id>/accounts/`.

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada conta bancária. Chave primária do model.
- account_number **(string)**: Número da conta gerado automaticamente de forma aleatória, com 6 dígitos, utilizando o valor do campo ID como seed. É acrescentado ao número, ainda, após um traço, um dígito verificador calculado com base na equação do Módulo 11, com pesos: 9, 8, 7, 6, 5, 4.
- customer **(integer)**: Obrigatório. Chave estrangeira que se refere ao cliente vinculado à conta bancária, através do ID do model [Cliente](#cliente).
- active_account **(boolean)**: Obrigatório. Status da conta, sendo verdadeiro (True) se a conta estiver ativa e falso (False) se a conta tiver sido encerrada.
- opening_date **(datetime.date)**: Obrigatório. Data de abertura da conta bancária. Após a criação da conta, não é possível alterar este dado.
- closure_date **(datetime.date)**: Data de encerramento da conta bancária. Só pode ser inserido se o valor do campo `active_account` for `False`, e vice-versa.

### Transação

O model `Transaction` disponibiliza, em suas propriedades, informações das transações bancárias.

Ao ser serializado, é possível criar e excluir transações, e consultar as já existentes. No entanto, não é possível realizar modificações em uma transação
já existente, tendo em vista que não deve haver a possibilidade de um cliente editar uma transação após a mesma ter sido agendada ou efetivada. No entanto,
há a possibilidade de exclusão, em casos de agendamento, ou em casos de estorno por exemplo.

Pode ser acessado pela rota: `/v1/transaction/`.
Também podem ser verificadas todas as contas de um mesmo cliente, pela rota: `/v1/account/<id>/transactions/`.

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada conta bancária. Chave primária do model.
- transaction_type **(string)**: Obrigatório. Tipo de transação, podendo ser uma das seguintes: 
  - "TI": Transferência entre contas do mesmo banco
  - "TE": Transferência para outro banco
  - "DE": Depósito
  - "RE": Recebimento em conta
  - "PG": Pagamento de guia ou boleto
  - "SQ": Saque
- date **(datetime.date)**: Obrigatório. Data de realização da transação.
- debit_account **(integer)**: Conta debitada na transação (referente ao ID da conta). Chave estrangeira vinculada ao model [Conta](#conta). É obrigatório caso o tipo de transação seja um dos seguintes: "TI", "TE", "PG", "SQ".
- credit_account **(integer)**: Conta debitada na transação (referente ao ID da conta). Chave estrangeira vinculada ao model [Conta](#conta). É obrigatório caso o tipo de transação seja um dos seguintes: "TI", "DE", "RE".
- amount **(float)**: Obrigatório. Valor da transação.

### Saldo

O model `Balance` disponibiliza, em suas propriedades, informações sobre o saldo da conta bancária.

Este model é instanciado automaticamente toda vez que uma instância do model [Conta](#conta) é criada.

Não há visualizações para este model, pois os dados serializados são visualizados juntamente aos do model [Conta](#conta) nas requisições GET.

#### Lista de propriedades

- account **(integer)**: ID da conta bancária a que se refere o saldo. Chave primária do model, sendo um campo `OneToOneField` vinculado ao model
[Conta](#conta). Ou seja, poderá haver uma instância do model `Balance` para cada instância do model `Account`, e vice-versa.
- balance **(float)**: Valor do saldo atual da conta bancária vinculada. O valor inicial, ao ser instanciado o objeto, será sempre 0.
o valor é atualizado sempre que uma nova transação é inserida, ou que uma transação já existente é excluída, através da consulta dos objetos do model
[Transação](#transação), sendo somado valor do campo `amount` de todas as transações cujo campo `credit_account` seja igual à account referida neste model,
subtraindo-se o valor do campo `amount` de todas as transações cujo campo `debit_account` seja igual à account referida neste model.

## Validações

### Validações Cliente

Validações do model [Cliente](#cliente) e suas serializações.

#### Lista de validações
- Validações da propriedade **customer_type**:
  - Valor não pode ser nulo ou em branco
  - Deverá ser uma das seguintes opções: "PF" ou "PJ"
  - Limite máximo de caracteres: 2
  
- Validações da propriedade **document_number**:
  - Valor não pode ser nulo ou em branco
  - Deverá ser uma string composta somente de números
  - Deverá ser único (não pode haver dois clientes com o mesmo `document_number`)
  - Deverá ter um número exato de caracteres: 11 se o valor da propriedade `customer_type` for "PF", 14 se for "PJ"
  - Os dois últimos dígitos deverão ser compatíveis com a equação dos dígitos verificadores estabelecida pela Receita Federal
  
- Validações da propriedade **name**:
  - Valor não pode ser nulo ou em branco
  - Deverá ter no mínimo 5 caracteres e no máximo 80 caracteres
  
- Validações da propriedade **phone_number**:
  - Valor não poderá ser nulo ou em branco
  - Para telefones fixos, deverá atender ao formato: "+00 00 0000-0000", sendo que o primeiro caractere da série de 4 dígitos antes do traço deverá estar entre 2 e 8
  - Para telefones celulares, deverá atender ao formato: "+00 00000-0000", sendo que o primeiro caractere da série de 5 dígitos antes do traço deverá ser 9
  - Limite máximo de caracteres: 17
   
- Validações da propriedade **email**:
  - Valor não poderá ser nulo ou em branco
  - Deverá ser um endereço de e-mail válido, contendo arroba e pelo menos um ponto após a arroba
  - Limite máximo de caracteres: 50
  
- Validações da propriedade **birthdate**:
  - Deverá ser uma data no formato: "AAAA-MM-DD"
  - Valor não poderá ser nulo ou branco se o valor da propriedade `customer_type` for "PF", ou seja, todos os clientes "pessoa física" devem ter uma data de nascimento informada
  - Valor deverá ser nulo se o valor da propriedade `customer_type` for "PJ", ou seja, os clientes "pessoa jurídica" não devem ter uma data de nascimento informada
  
- Validações da propriedade **zip_code**:
  - Deverá atender ao formato: "00000-000"
  - Deverá ser um CEP existente, com base em consulta no API VIACEP
  - Limite máximo de caracteres: 9

- Validações da propriedade **door_number**:
  - Valor não poderá ser nulo ou branco
  - Deverá ter entre 1 e 10 caracteres

- Validações da propriedade **complement**:
  - Limite máximo de caracteres: 30

### Validações Conta

Validações do model [Conta](#conta) e suas serializações.

#### Lista de validações
- Validações da propriedade **account_number*:
  - Valor não poderá ser nulo ou em branco
  - Deverá ser único (não pode haver duas contas com o mesmo `account_number`)
  - Limite de caracteres: 8
  
- Validações da propriedade **customer**:
  - Valor não poderá ser nulo ou em branco (exceto nos casos em que o objeto `Customer` vinculado for excluído após a criação da conta)
  - Deverá ser um valor inteiro referente
  - Deverá se referir a um ID de um cliente existente entre os objetos da classe `Customer`
  - Não poderá ser alterado após a criação da conta
  
- Validações da propriedade **active_acount**:
  - Valor não poderá ser nulo ou em branco
  - Não poderá ser `true` se houver valor diferente de `null` na propriedade `closure_date`, ou seja, a conta não poderá estar ativa se houver uma data de encerramento
  - Não poderá ser `false` se a propriedade `closure_date` tiver o valor `null`, ou seja, a conta não poderá ser encerrada sem uma data de encerramento
  - Não poderá ser `false` se a propriedade `balance` do objeto `Balance` vinculado à mesma conta não tiver o valor igual a `0.0`
  - Não poderá ser alterada para `true` após já ter sido registrada como `false`, ou seja, não é possível reabrir uma conta já encerrada

- Validações da propriedade **opening_date**:
  - Valor não poderá ser nulo ou branco
  - Deverá ser uma data no formato: "AAAA-MM-DD"
  - Não poderá ser alterado após a criação da conta
  
- Validações da propriedade **closure_date**:
  - Deverá ser uma data no formato: "AAAA-MM-DD"
  - Deverá ser uma data mais recente do que a constante na propriedade `opening_date`, ou seja, a data de encerramento da conta deverá ser posterior à data de abertura
  - Deverá ser uma data mais recente do que a constante na propriedade `date` do objeto `Transaction` mais recente cuja propriedade `debit_account` ou `credit_account` esteja vinculada a esta conta, ou seja, não poderá ser realizado o encerramento da conta em uma data anterior à data da última transação realizada nesta conta
  - Não poderá ser diferente de `null` se a propriedade `active_account` tiver o valor `true`, ou seja, a conta não poderá estar ativa se houver uma data de encerramento
  - Não poderá ser `null` se a propriedade `active_account` tiver o valor `false`, ou seja, a conta não poderá ser encerrada sem uma data de encerramento
  - Não poderá ser alterada para nulo após já ter sido registrada uma data de encerramento para a conta, ou seja, não é possível reabrir uma conta já encerrada

### Validações Transação

Validações do model [Transação](#transação) e suas serializações.

#### Lista de validações

- Validações da propriedade **transaction_type**:
  - Valor não pode ser nulo ou em branco
  - Deverá ser uma das seguintes opções: "TI", "TE", "DE", "RE", "PG", "SQ"
  - Limite máximo de caracteres: 2

- Validações da propriedade **date**:
  - Valor não poderá ser nulo ou em branco
  - Deverá ser uma data no formato: "AAAA-MM-DD"
  - Deverá ser mais recente do que a data de abertura das contas de débito (propriedade `debit_account`) e/ou crédito (propriedade `credit_account`) vinculadas à transação

- Validações da propriedade **debit_account**:
  - Chave estrangeira referente à propriedade `account_number` da classe `Account`
  - Deverá obrigatoriamente ser preenchida se o valor da propriedade `transaction_type` for um dos seguintes: "TI", "TE", "PG", "SQ", e não deverá ser preenchida caso contrário
  - Não é possível realizar débito em uma conta cujo campo `active_account` seja `false`, ou seja, não é possível realizar uma transação em uma conta que já tenha sido encerrada

- Validações da propriedade **credit_account**:
  - Chave estrangeira referente à propriedade `account_number` da classe `Account`
  - Deverá obrigatoriamente ser preenchida se o valor da propriedade `transaction_type` for um dos seguintes: "TI", "DE", "RE" e não deverá ser preenchida caso contrário
  - Não é possível realizar crédito em uma conta cujo campo `active_account` seja `false`, ou seja, não é possível realizar uma transação em uma conta que já tenha sido encerrada

- Validações da propriedade **amount**:
  - Valor não poderá ser nulo ou em branco
  - Deverá ter no máximo duas casas decimais

## Filtros, Ordenação e Pesquisa de Dados

### Filtros Cliente

Filtros, ordenação e pesquisa de dados que podem ser realizados na visualização do model [Cliente](#cliente).

Para utilização dos filtros, ordenações e pesquisas, acrescentar a route do filtro desejado, após `/v1/customer/?`.

Para utilização de múltiplos filtros, ordenações e/ou pesquisas, acrescentar `&` entre as routes dos filtros desejados.

#### Lista de filtros

- Filtros da propriedade (**name**):
  - Nome completo ou razão social contém
    - Route: `name__icontains=`

- Filtros da propriedade (**customer_type**)
  - Tipo de cliente (_PF_ ou _PJ_)
    - Route: `customer_type=`

- Filtros da propriedade (**birthdate**)
  - Data de nascimento é maior ou igual a
    - Route: `birthdate__gte=`
  - Data de nascimento é menor ou igual a
    - Route: `birthdate_date__lte=`
  - Data de nascimento é igual a
    - Route: `birthdate=`

#### Lista de ordenações de dados

- Ordenação pela propriedade (**name**)
  - Ascendente
    -  `ordering=name`
  - Descendente
    -  `ordering=-name`

#### Lista de pesquisas de dados

- Route: `search=`
  - Pesquisa pela propriedade (**name**)
  - Pesquisa pela propriedade (**document_number**)

### Filtros Conta

Filtros, ordenação e pesquisa de dados que podem ser realizados na visualização do model [Conta](#conta).

Para utilização dos filtros, ordenações e pesquisas, acrescentar a route do filtro desejado, após `/v1/customer/?`.

Para utilização de múltiplos filtros, ordenações e/ou pesquisas, acrescentar `&` entre as routes dos filtros desejados.

#### Lista de filtros

- Filtros da propriedade (**active_account**):
  - Conta ativa (_true_ ou _false_)
    - Route: `active_account=`

- Filtros da propriedade (**opening_date**)
  - Data de abertura é maior ou igual a
    - Route: `opening_date__gte=`
  - Data de abertura é menor ou igual a
    - Route: `opening_date__lte=`
  - Data de abertura é igual a
    - Route: `opening_date=`

- Filtros da propriedade (**closure_date**)
  - Data de encerramento é maior ou igual a
    - Route: `opening_date__gte=`
  - Data de encerramento é menor ou igual a
    - Route: `opening_date__lte=`
  - Data de encerramento é igual a
    - Route: `opening_date=`

- Filtros da propriedade (**customer**)
  - ID do cliente 
    - Route `customer=`
  - Lista de IDs dos clientes separados por vírgula
    - Route `customer__in=`

#### Lista de ordenações de dados



#### Lista de pesquisas de dados

### Filtros Transação

Filtros, ordenação e pesquisa de dados que podem ser realizados na visualização do model [Transação](#transação).

#### Lista de filtros

#### Lista de ordenações de dados

#### Lista de pesquisas de dados

