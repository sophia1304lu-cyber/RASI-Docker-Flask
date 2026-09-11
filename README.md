# RASI - Docker com aplicação Python/Flask

Trabalho desenvolvido para a disciplina de Redes e Administração de Sistemas (RASI), do Instituto Federal de São Paulo (IFSP).

## Objetivo

O objetivo deste trabalho é demonstrar a criação de uma máquina virtual com Ubuntu Server, o acesso remoto utilizando SSH e a utilização do Docker para executar uma aplicação web desenvolvida em Python com Flask.

A aplicação foi containerizada utilizando a imagem base obrigatória `python:3.14-slim`.

## Tecnologias utilizadas

- Ubuntu Server
- VirtualBox
- SSH
- Docker
- Python
- Flask

## Estrutura do projeto

```text
RASI-Docker-Flask/
├── app.py
├── requirements.txt
└── Dockerfile
```

## Aplicação Flask

A aplicação possui três páginas:

- `/` - Página inicial
- `/sobre` - Página sobre o projeto
- `/contato` - Página de contato

## Dockerfile

O container utiliza a imagem `python:3.14-slim` como imagem base.

O Dockerfile realiza as seguintes etapas:

1. Define a imagem base.
2. Define o diretório de trabalho.
3. Copia o arquivo `requirements.txt`.
4. Instala o Flask.
5. Copia o arquivo `app.py`.
6. Expõe a porta 5000.
7. Executa a aplicação Flask.

## Comandos utilizados

### Criar a imagem Docker

```bash
docker build -t minha-flask .
```

### Executar o container

```bash
docker run -d -p 5000:5000 --name meu-flask minha-flask
```

### Verificar os containers em execução

```bash
docker ps
```

### Visualizar os logs da aplicação

```bash
docker logs meu-flask
```

## Acesso à aplicação

A aplicação utiliza a porta 5000 e possui as seguintes páginas:

- `/`
- `/sobre`
- `/contato`

## Autoras

Sophia Gonçalves e Júlia Gomes

Projeto desenvolvido para a disciplina de RASI - IFSP Campus Campos do Jordão.
