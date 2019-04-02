# cidadaobr
**Esse projeto está desatualizado e será refeito em breve!**

Gerador de dados aleatórios de um cidadão brasileiro. Ideal para desenvolvedores, mas sua utilidade depende de quem o usar

## Começando
Essas instruções vão te garantir uma cópia do projeto rodando em sua máquina local para desenvolvimento e testes, apenas.

### Pré-requisitos
* Python >= 2.7 ou Python >= 3.6
* Módulos Python:
	* [Requests](https://docs.python-requests.org/pt_BR/latest/)
	* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Instalação
Pelo pip (recomendado):
```
pip install cidadaobr
```
Pelo git:
```
git clone https://github.com/yanorestes/cidadaobr.git
```

### Como usar
#### Instância da classe CidadaoBrasileiro
* Construtor:
	* nome (str - opcional)
	* data_nascimento (str -- AAAA/MM/DD obrigatoriamente - opcional)
	* estado (str ex. SP/RJ/MG... - opcional)
* Atributos:
	* nome (str)
	* data_nascimento (datetime.date)
	* idade (int)
	* cpf (str)
	* rg (str -- Por enquanto apenas para cidadãos paulistas)
	* endereco (Endereco)
		* estado (str)
		* cidade (str)
		* bairro (str)
		* logradouro (str)
		* numero (int)
		* ibge (str)
		* ddd (str)
	* telefone_fixo (str)
	* celular (str)
* Métodos:
	* \_\_repr\_\_ (retorna uma string contendo todos os dados formatados)
	* json (retorna um dicionário contendo todos os dados)
	* \_\_getitem\_\_ (param: index -- retorna o dado buscado no dicionário json com o index do parâmetro)

#### Exemplo de código
Exemplo 1:
```python
from cidadaobr import CidadaoBrasileiro

cidadao = CidadaoBrasileiro()
print(cidadao)
```
Resultado (Ex.):
```
Nome: Rosana Cerveira
Data de Nascimento: 1979-02-14
Idade: 38
CPF: 63563459428
RG: None
Endereço:
	Brasil - ES - Cariacica
	Campina Grande
	Rua Cabo Frio, 332
	IBGE: 3201308
Telefone Fixo: +55 27 85798533
Telefone Celular: +55 27 944737310
```

Exemplo 2:
```python
from cidadaobr import CidadaoBrasileiro

cidadao = CidadaoBrasileiro(nome='Yan Orestes', data_nascimento='23/10/2000', estado='SP')
print(c.json())
print('\n' + cidadao['nome'])
```
Resultado (Ex.):
```
{'nome': 'Yan Orestes', 'nascimento': '23/10/2000', 'idade': 17, 'cpf': '94275784243', 'pais': 'Brasil', 'estado': 'SP', 'cidade': 'Itapira', 'rg': '839280120', 'bairro': 'Centro', 'logradouro': 'Rua Doutor Mário da Fonseca', 'endereco_numero': 767, 'endereco_ibge': '3522604', 'fixo': '+55 19 83968836', 'celular': '+55 19 997928407'}

Yan Orestes
```

## Controle de Versão
Utilizamos o git para controle de versão. Cheque as [tags nesse repositório](https://github.com/yanorestes/cidadaobr/tags) para ver as versões disponíveis.

## Autores
* **Yan Orestes - nbdy**

## Licença
Este projeto está licenciado sob a Licença MIT - veja [LICENSE.txt](LICENSE.txt)
