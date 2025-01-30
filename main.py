from fastapi import FastAPI, HTTPException
from loguru import logger
import httpx
from celery_app import save_advice_to_file

app = FastAPI()

# Configuração do Loguru para FastAPI
logger.add("logs/loguru_fastapi.log", rotation="1 MB", level="DEBUG")

# Base URL da API pública
ADVICE_API_URL = "https://api.adviceslip.com"

# Rota para pegar um conselho aleatório
@app.get("/advice")
async def get_random_advice():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{ADVICE_API_URL}/advice")
            response.raise_for_status()  # Levanta exceção se a resposta for de erro
            data = response.json()

            advice = data["slip"]["advice"]
            # Enviar conselho para a fila do Celery para salvar em um arquivo
            save_advice_to_file.delay(advice)

            logger.info(f"Conselho retornado: {advice}")
            return {"advice": advice}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao obter conselho: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail="Erro ao obter conselho")
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Rota para pegar um conselho por ID específico
@app.get("/advice/{advice_id}")
async def get_advice_by_id(advice_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{ADVICE_API_URL}/advice/{advice_id}")
            response.raise_for_status()
            data = response.json()

            advice = data["slip"]["advice"]
            # Enviar conselho para a fila do Celery para salvar em um arquivo
            save_advice_to_file.delay(advice)

            logger.info(f"Conselho retornado pelo ID {advice_id}: {advice}")
            return {"advice": advice}
    except httpx.HTTPStatusError as e:
        logger.error(f"Erro ao obter conselho por ID {advice_id}: {str(e)}")
        raise HTTPException(status_code=e.response.status_code, detail="Erro ao obter conselho")
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
