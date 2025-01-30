from fastapi import FastAPI, HTTPException
import httpx
from loguru import logger

app = FastAPI()

# Base URL of the public API
ADVICE_API_URL = "https://api.adviceslip.com"

# Configure Loguru
logger.add("file.log", rotation="1 week", retention="1 month", level="INFO")

# Route to get a random advice
@app.get("/advice")
async def get_random_advice():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{ADVICE_API_URL}/advice")
            response.raise_for_status()  # Raises an exception if the response is an error
            data = response.json()
            logger.info("Retrieved random advice successfully.")
            return {"advice": data["slip"]["advice"]}
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP status error occurred: {e}")
        raise HTTPException(status_code=e.response.status_code, detail="Error retrieving advice")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

# Route to get advice by specific ID
@app.get("/advice/{advice_id}")
async def get_advice_by_id(advice_id: int):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{ADVICE_API_URL}/advice/{advice_id}")
            response.raise_for_status()
            data = response.json()
            logger.info(f"Retrieved advice by ID {advice_id} successfully.")
            return {"advice": data["slip"]["advice"]}
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP status error occurred: {e}")
        raise HTTPException(status_code=e.response.status_code, detail="Error retrieving advice")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

# TODO: Docker

# TODO: Add (https://pypi.org/project/celery/) ADD advices on a queue;
