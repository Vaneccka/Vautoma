import aiohttp
import asyncio
import json
import logging

logger = logging.getLogger(__name__)

# === Модель 1: DeepSeek через ProxyAPI ===
async def send_deepseek_request(prompt: str, api_key: str) -> str:
    api_url = "https://api.proxyapi.ru/deepseek/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Ты эффективный и точный deepseek помощник."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4000
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, headers=headers, json=payload, timeout=200) as response:
                response_text = await response.text()
                if response.status != 200:
                    return f"❌ Ошибка от DeepSeek API: {response.status}"

                data = json.loads(response_text)
                if "choices" in data and len(data["choices"]) > 0:
                    # Удалим лишние символы (например, markdown)
                    return data["choices"][0]["message"]["content"].replace("#", "").replace("**", "").replace("- **", "")
                else:
                    return f"⚠️ Неправильный формат ответа: {data}"
    except Exception as e:
        return f"Ошибка запроса к DeepSeek: {str(e)}"

# === Модель 2: GPT-4o (через ProxyAPI как OpenAI) ===
async def send_openai_request(prompt: str, api_key: str) -> str:
    api_url = "https://api.proxyapi.ru/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Ты эффективный и точный openai помощник."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4000
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, headers=headers, json=payload, timeout=200) as response:
                response_text = await response.text()
                if response.status != 200:
                    return f"❌ Ошибка от OpenAI API: {response.status}"

                data = json.loads(response_text)
                if "choices" in data and len(data["choices"]) > 0:
                    return data["choices"][0]["message"]["content"]
                else:
                    return f"⚠️ Неправильный формат ответа: {data}"
    except Exception as e:
        return f"Ошибка подключения к OpenAI ProxyAPI: {str(e)}"
