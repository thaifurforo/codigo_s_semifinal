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

[Acesse aqui as especificações OpenAPI Swagger](docs/swagger.json)

## Funcionalidades
- Criação, atualização, consulta e exclusão de clientes
- Criação, atualização e consulta de contas bancárias
- Criação, consulta e exclusão de transações bancárias
- Consulta de contas bancárias por cliente
- Consulta de transações bancárias por conta

## Contato
Em caso de problemas, favor abrir uma [issue](https://github.com/thaifurforo/codigo_s_semifinal/issues).

## Requisitos
A versão do Python utilizada para o desenvolvimento desta API foi a 3.10.4.

As bibliotecas utilizadas para o desenvolvimento desta API constam em [requirements.txt](requirements.txt).

Para realizar a instalação das mesmas, em seu ambiente virtual, digite o comando: `pip install -r requirements.txt`

## Lista de Models
- [Model com as propriedades do cliente](#cliente)
- [Model com as propriedades dos endereços registrados](#endereço)
- [Model com as propriedades da conta bancária](#conta)
- [Model com as propriedades do saldo atual da conta bancária](#saldo)
- [Model com as propriedades da transação bancária](#transação)

## Models

### Cliente

O model `Customer` disponibiliza, em suas propriedades, informações de um cliente.

Ao ser serializado, é possível inserir novos clientes, realizar atualizações nos dados dos clientes já existentes,
consultar os clientes e excluí-los, considerando as normas da LGPD.

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada cliente.
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

Não há View para este model, pois os dados serializados são visualizados juntamente aos do model [Cliente](#cliente) nas requisições GET.

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada endereço.
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

#### Lista de propriedades

- id **(integer)**: ID gerado automaticamente para cada conta bancária.
- account_number **(string)**: Número da conta gerado automaticamente de forma aleatória, utilizando o valor do campo ID como seed. É acrescentado ao número,
ainda, um dígito verificador calculado com base na equação do Módulo 11, com pesos: 9, 8, 7, 6, 5, 4.
- customer **(integer)**: Obrigatório. Foreign Key que se refere ao cliente vinculado à conta bancária, através do ID do model [Cliente](#cliente).
- active_account **(boolean)**: Obrigatório. Status da conta, sendo verdadeiro (True) se a conta estiver ativa e falso (False) se a conta tiver sido encerrada.
- opening_date **(datetime.date)**: Obrigatório. Data de abertura da conta bancária. Após a criação da conta, não é possível alterar este dado.
- closure_date **(datetime.date)**: Data de encerramento da conta bancária. Só pode ser inserido se o valor do campo `active_account` for `False`, e vice-versa.

### Transação

O model `Transaction`

#### Lista de propriedades

-

### Saldo

O model `Balance` disponibiliza, em suas propriedades, informações sobre o saldo da conta bancária.

Este model é instanciado automaticamente toda vez que uma instância do model [Conta](#conta) é criada.

Não há View para este model, pois os dados serializados são visualizados juntamente aos do model [Conta](#conta) nas requisições GET.

#### Lista de propriedades

- account **(integer)**: ID da conta bancária a que se refere o saldo. Primary key do model, sendo um campo `OneToOneField` vinculado ao model
[Conta](#conta). Ou seja, poderá haver uma instância do model `Balance` para cada instância do model `Account`, e vice-versa.
- balance **(float)**: Valor do saldo atual da conta bancária vinculada. O valor inicial, ao ser instanciado o objeto, será sempre 0.
o valor é atualizado sempre que uma nova transação é inserida, ou que uma transação já existente é excluída, através da consulta dos objetos do model
[Transação](#transação), sendo somado valor do campo `amount` de todas as transações cujo campo `credit_account` seja igual à account referida neste model,
subtraindo-se o valor do campo `amount` de todas as transações cujo campo `debit_account` seja igual à account referida neste model.

