# Python Technical Challenge

Este é um projeto que implementa duas tarefas em Python, nele há dois arquivos principais e o os arquivos de testes.

## Descrição do Projeto

1. **Contracts**: Implementa uma classe para lidar com contratos e um método para encontrar os N maiores devedores que ainda não renegociaram seus débitos.
2. **Orders**: Implementa uma classe para pedidos de agencias próximas para otimizar o número de viagens de carro-forte necessárias no atendimento das requisições.

## Arquivos do Projeto

- contracts.py: classes `Contract` e `Contracts`
- orders.py: classe `Orders`
- test_contracts.py: Testa a funcionalidade da classe `Contract` e `Contracts`.
- test_orders.py: Testa a funcionalidade da classe `Orders`.

## Requisitos do Projeto

As tarefas foram implementadas de acordo com os seguintes requisitos:

- Uso de boas práticas de programação.
- Aderência aos padrões da linguagem Python.
- Documentação necessária.
- Performance em diferentes cenários.

## Como Executar os Testes

Para a execução dos testes foi usado o `pytest`, Instale o pytest em seu ambiente:

```bash
pip install pytest ou
poetry add pytest

### Testes para `contracts.py`

- `test_get_top_N_open_contracts_default`: Testa se a função `get_top_N_open_contracts` retorna os N maiores devedores quando houver contratos, e se alguns foram renegociados.
- `test_get_top_N_open_contracts_empty_list`: Testa se a função `get_top_N_open_contracts` retorna uma lista vazia quando não tem contratos.
- `test_get_top_N_open_contracts_with_fewer_contracts`: Testa se a função `get_top_N_open_contracts` retorna os maiores devedores se houver menos contratos do que N.

### Testes para `orders.py`

- `test_default_scenario`: Testa se a função `combine_orders` retorna o número minimo de viagens corretamente em um cenário padrão.
- `test_orders_empty_requests`: Testa se a função `combine_orders` retorna 0 viagens quando não há requisições.
- `test_orders_with_maximum_request`: Testa se a função `combine_orders` retorna o número correto de viagens quando todas as requisições tem o valor máximo permitido.
