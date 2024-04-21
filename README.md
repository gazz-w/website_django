# Projeto Website

Este projeto é uma aplicação de um website desenvolvido em Django para uma clínica. A principio temos as páginas estáticas, porém o intuito é desenvolver mais funcionalidades ao longo do tempo.

## Configuração do Ambiente

Siga as instruções abaixo para configurar o ambiente de desenvolvimento e executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Este projeto foi criado com Python 3.10.

### Configuração do Ambiente Virtual

1. Clone o repositório para sua máquina local.
2. Navegue até a pasta do projeto clonado.
3. Crie um ambiente virtual usando o seguinte comando:

```bash
python -m venv venv
```
4. Ative o ambiente virtual: 
No windows:
```bash
.\venv\Scripts\activate
```
No unix ou MacOs:
```bash:
source venv/bin/activate
```
## Configuração do Ambiente

Siga as instruções abaixo para configurar o ambiente de desenvolvimento e executar o projeto localmente.

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Este projeto foi testado com Python 3.10.

### Configuração do Ambiente Virtual

1. Clone o repositório para sua máquina local.
2. Navegue até a pasta do projeto clonado.
3. Crie um ambiente virtual usando o seguinte comando:

windows:

```bash
python -m venv venv
```

No unix ou MacOS:

``` bash
source venv/bin/activate
```

### Configuração da Secret Key do Django

1. Gere uma nova SECRET_KEY executando o seguinte comando em seu Python shell:

```bash
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

```

2. Adicione a SECRET_KEY gerada ao seu arquivo .env ou diretamente no seu settings.py:
 - '.env':
```plaintext 
SECRET_KEY='sua_nova_secret_key_aqui'
```
- settings.py:

```python
SECRET_KEY = 'sua_nova_secret_key_aqui'
```


### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Execução do projeto:

```bash
python manage.py runserver
```