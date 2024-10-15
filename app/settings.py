""" Read settings from environment variables. """
import os
from pydantic_settings import BaseSettings     # type: ignore


class Settings(BaseSettings):
    # general settings
    temperature: float = 0.4        # be a bit creative but not too much
    max_tokens: int = 4096          # max number of tokens to generate  # XXX FIXME: this is model dependent
    top_p: float = 1.0              # top p for nucleus sampling
    top_k: int = 1                  # top k for nucleus sampling
    frequency_penalty: float = 0.0  # no frequency penalty
    presence_penalty: float = 0.0   # no presence penalty

    # openai settings
    openai_api_key: str = os.getenv("OPENAI_API_KEY", '')
    openai_model: str = "gpt-4o-mini"
    openai_base_url: str = ""

    # ollama settings
    ollama_api_key: str = "foobar"  # not used
    ollama_num_gpu: int = 3
    ollama_base_url: str = "http://nanu:11434"
    ollama_model: str = "universal_translator:mistral-nemo-12b"

    # anthropic settings
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", '')
    anthropic_model: str = "claude-3-5-sonnet"
    anthropic_base_url: str = "https://api.anthropic.com/v1/messages"

    # gemini settings
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", '')
    gemini_model: str = "gemini-1.5-flash"
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta"

    # groq settings
    groq_api_key: str = os.getenv("GROQ_API_KEY", '')
    groq_model: str = "mixtral-8x7b-32768"
    groq_base_url: str = "https://api.groq.com/openai/v1/chat/completions"

    # deepL settings
    deepl_api_key: str = os.getenv("DEEPL_API_KEY", '')
    deepl_model: str = "deepl-pro"
    deepl_base_url: str = "https://api-free.deepl.com/v2/translate"


settings = Settings()
