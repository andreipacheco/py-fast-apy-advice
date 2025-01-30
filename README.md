
# 🌟 FastAPI Advice Generator 🌟

Este é um projeto simples de **FastAPI** que consome a [API pública Advice Slip](https://api.adviceslip.com/#endpoint-random) para fornecer conselhos aleatórios e específicos. 🚀

## ✨ Funcionalidades
- 🔄 **Conselho Aleatório**: Obtenha um conselho aleatório.
- 🎯 **Conselho por ID**: Obtenha um conselho específico pelo seu ID.
- 📄 **Documentação Interativa**: Acesse a interface Swagger para testar os endpoints de forma interativa.
- 🗂️ **Conselho em Background com Celery**: Use filas do Celery para salvar conselhos aleatórios em um arquivo no background.

## ⚙️ Pré-requisitos

- 🐍 **Python 3.8+**
- 📦 **pip** (para gerenciar pacotes)
- 🌐 **FastAPI** e **Uvicorn**
- 📝 Loguru para logs melhorados

## 🚀 Instalação

Siga os passos abaixo para configurar e rodar o projeto localmente:

1. **Clone o repositório** 📂
   ```bash
   git clone https://github.com/seu-usuario/fastapi-advice.git

## 🛠️ Tecnologias Utilizadas
- FastAPI ⚡ - Framework para desenvolvimento de APIs rápidas.
- Uvicorn 🌐 - Servidor ASGI para rodar a aplicação FastAPI.
- HTTPX 📨 - Cliente HTTP para fazer chamadas à API Advice Slip.
- Celery 🟢 - Sistema de filas para execução de tarefas assíncronas.
- Redis 🔗 - Broker utilizado pelo Celery para gerenciamento de filas.
- Loguru 📝 - Biblioteca para gerenciamento de logs detalhados.

## 📝 Licença
Este projeto é distribuído sob a licença APACHE. Fique à vontade para usar e modificar conforme necessário. 😊