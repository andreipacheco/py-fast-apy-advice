from celery import Celery
from loguru import logger
import os

# Cria a instância Celery
celery_app = Celery('celery_app', broker='redis://localhost:6379/0')

# Configuração do Loguru nos workers Celery
logger.add("logs/loguru_celery.log", rotation="1 MB", level="DEBUG")

# Função para configurar o Loguru nos processos de workers Celery
@celery_app.on_after_configure.connect
def setup_loguru(**kwargs):
    logger.info("Loguru configurado nos workers do Celery")

@celery_app.task
def save_advice_to_file(advice: str):
    try:
        file_path = "advice_log.txt"
        # Escreve o conselho em um arquivo
        with open(file_path, "a") as file:
            file.write(f"{advice}\n")
        logger.info(f"Conselho salvo no arquivo: {advice}")
    except Exception as e:
        logger.error(f"Erro ao salvar conselho no arquivo: {str(e)}")
        raise e
