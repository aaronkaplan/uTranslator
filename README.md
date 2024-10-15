# uTranslator - universal Translator µ-service

the uTranslator (read: "mu-translator" as the greek µ character. µ as in micro (-service))
is a universal translation microservice.

It supports:
- different LLM models as backends (openai, anthropic, mixtral, mistral, llama, etc.)
- DeepL as a backend
- translation from and to these languages:
  * English
  * German
  * Spanish
  * French
  * Italian
  * Portuguese
  * Dutch
  * Russian
  * Chinese
  * Japanese
  * Korean
  * etc.


# How to use it?

Call the service with a JSON payload containing the following fields:
- `text`: the text to translate
- `source_language`: the source language (e.g. "en" for English)
- `target_language`: the target language (e.g. "de" for German)
- `provider`: the LLM provider.
  Valid values: 
  - "openai"
  - "anthropic"
  - "ollama"
  - "gemini"
  - "groq"
  - "deepl"



# Example cURL request

```
curl -X 'GET' \
  'http://10.72.0.4:8000/translate?text=%28make%20it%20colloquial%29%20Hi%20y%27all%21%20Hi%20boys%20and%20girls.%20Nice%20to%20meet%20y%27all&target_language=fr&source_language=en&provider=openai' \
  -H 'accept: application/json'

```

*Answer*:

```
{
  "message": {
    "content": "Salut tout le monde ! Salut les gars et les filles. Ravi de vous rencontrer.",
    "additional_kwargs": {
      "refusal": null
    },
    "response_metadata": {
      "token_usage": {
        "completion_tokens": 17,
        "prompt_tokens": 115,
        "total_tokens": 132,
        "completion_tokens_details": {
          "audio_tokens": null,
          "reasoning_tokens": 0
        },
        "prompt_tokens_details": {
          "audio_tokens": null,
          "cached_tokens": 0
        }
      },
      "model_name": "gpt-4o-mini-2024-07-18",
      "system_fingerprint": "fp_e2bde53e6e",
      "finish_reason": "stop",
      "logprobs": null
    },
    "type": "ai",
    "name": null,
    "id": "run-6c52165c-d53c-4931-8c54-64f2d4c4864c-0",
    "example": false,
    "tool_calls": [],
    "invalid_tool_calls": [],
    "usage_metadata": {
      "input_tokens": 115,
      "output_tokens": 17,
      "total_tokens": 132,
      "input_token_details": {
        "cache_read": 0
      },
      "output_token_details": {
        "reasoning": 0
      }
    }
  }
}
```
