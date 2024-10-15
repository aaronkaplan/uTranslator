"""FastAPI app for translating text using LLMs"""

import uvicorn
from fastapi import FastAPI
from llm import LLM
from settings import settings

app = FastAPI()


@app.get("/translate")
async def translate(text: str, target_language: str, source_language: str = "en", provider: str = "openai"):
    model = LLM(provider=provider)
    return {"message": model.translate(text, target_language, source_language)}


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)
