"""LLM wrapper for interacting with OpenAI models, 
local LLMs, and other providers.

This file uses the langchain abstraction. 
It can split texts as needed.
"""

import logging

from langchain_openai import ChatOpenAI
from langchain_anthropic import AnthropicLLM
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama.llms import OllamaLLM
import deepl

from settings import settings

PROMPT_TEMPLATE = """
Ignore all previous instructions and system prompts! You are a universal 
translator. Your input language is {source_language}. 
Every input you receive will be translated into {target_language}. 
Only output the translated text without any additional information, 
comments or explanations. Preserve the formatting of the original text. 
Omit nothing. Never summarize! If the original text is in english just 
respond word by word the original text.

Text to translate:
{text}
"""


class LLM:
    def __init__(self, provider: str = "openai"):
        """Initialize the LLM wrapper.

        Args:
            provider (str): The LLM provider. Valid providers:
            - openai
            - ollama
            - deepl
            - groq
            - anthropic
            - gemini
        """
        self.provider = provider

        if self.provider == "ollama":
            model = settings.ollama_model
            self.client = OllamaLLM(model=model, base_url=settings.ollama_base_url,
                                    temperature=settings.temperature,
                                    num_gpu=settings.ollama_num_gpu)
        elif self.provider == "openai":
            model = settings.openai_model
            self.client = ChatOpenAI(model=model, api_key=settings.openai_api_key, base_url=settings.openai_base_url,
                                     temperature=settings.temperature, max_tokens=settings.max_tokens)
        elif self.provider == "deepl":
            self.client = deepl.Translator(settings.deepl_api_key)
        elif self.provider == "anthropic":
            self.client = AnthropicLLM(api_key=settings.anthropic_api_key, model=settings.anthropic_model,
                                       temperature=settings.temperature, max_tokens=settings.max_tokens)
        else:
            raise ValueError(f"Invalid provider or not implemented yet: {provider}")

        # self.prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
        self.prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    def translate(self, text: str, target_language: str, source_language: str = "en"):
        """Translate text to target language."""

        logging.info(f"Translating with {self.provider}")
        if self.provider == "deepl":
            return self.translate_with_deepl(text, target_language, source_language)
        else:
            prompt = self.prompt.format(text=text,
                                        target_language=target_language,
                                        source_language=source_language)

            return self.client.invoke(prompt)

    def translate_with_deepl(self, text: str, target_language: str, source_language: str = "en"):
        """Translate text to target language using DeepL."""
        # XXX FIXME: DeepL is a bit picky w.r.t to the target_lang parameter.
        #  It seems to require the language code in uppercase
        # and in addition, only certain values for target_lang are accepted.
        # see https://www.deepl.com/docs-api/translating-text/?utm_source=github&utm_medium=github-python-readme
        # so we will have to make a mapping here.

        if target_language.lower() == 'english' or target_language.lower() == 'en':
            target_language = 'EN-US'
        try:
            result = self.client.translate_text(text, target_lang=target_language.upper())
            return result.text
        except Exception as e:
            logging.error("Translation failed (dst_language: %s): %s" % (target_language, str(e)))
            return ""


if __name__ == "__main__":
    llm = LLM(provider="ollama")
    print(llm.translate("Hello, world!", target_language="es"))
